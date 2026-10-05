const chai = require("chai");
const chaiHttp = require("chai-http");
const server = require("../app");
const Order = require("../models/order");
const connection = require("../connection");
const should = chai.should();

chai.use(chaiHttp);

describe("Goldman Sachs Limit Order Book & Matching Engine API", () => {
  beforeEach(async () => {
    await connection.initialize();
  });

  after(async () => {
    await Order.drop();
  });

  describe("POST /orders - Order Validation", () => {
    it("should return 400 if symbol is missing, lowercase, or > 5 chars", async () => {
      const res1 = await chai.request(server).post("/orders").send({
        symbol: "aapl",
        side: "BUY",
        price: 150,
        quantity: 10,
      });
      res1.should.have.status(400);

      const res2 = await chai.request(server).post("/orders").send({
        symbol: "VERYLONGSYMBOL",
        side: "BUY",
        price: 150,
        quantity: 10,
      });
      res2.should.have.status(400);
    });

    it("should return 400 if side is invalid", async () => {
      const res = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "HOLD",
        price: 350,
        quantity: 10,
      });
      res.should.have.status(400);
    });

    it("should return 400 if price <= 0 or quantity <= 0 or quantity is float", async () => {
      const res1 = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "BUY",
        price: -10,
        quantity: 10,
      });
      res1.should.have.status(400);

      const res2 = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "BUY",
        price: 100,
        quantity: 0,
      });
      res2.should.have.status(400);

      const res3 = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "BUY",
        price: 100,
        quantity: 10.5,
      });
      res3.should.have.status(400);
    });
  });

  describe("POST /orders - Order Creation & Matching Engine", () => {
    it("should create an OPEN order when no matching opposite orders exist", async () => {
      const res = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "BUY",
        price: 350.0,
        quantity: 100,
      });

      res.should.have.status(201);
      res.body.should.have.property("id");
      res.body.status.should.eql("OPEN");
      res.body.remainingQuantity.should.eql(100);
      res.body.price.should.eql(350.0);
    });

    it("should fully match and fill orders when crossing prices with exact quantities", async () => {
      // 1. Post a SELL order: 100 shares @ $350
      const sellRes = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "SELL",
        price: 350.0,
        quantity: 100,
      });
      sellRes.should.have.status(201);

      // 2. Post a BUY order: 100 shares @ $350
      const buyRes = await chai.request(server).post("/orders").send({
        symbol: "GS",
        side: "BUY",
        price: 350.0,
        quantity: 100,
      });
      buyRes.should.have.status(201);
      buyRes.body.status.should.eql("FILLED");
      buyRes.body.remainingQuantity.should.eql(0);

      // Verify the SELL order in database is now FILLED as well
      const updatedSell = await Order.findByPk(sellRes.body.id);
      updatedSell.status.should.eql("FILLED");
      updatedSell.remainingQuantity.should.eql(0);
    });

    it("should handle partial matching when incoming order is smaller than book order", async () => {
      // 1. Post a SELL order: 200 shares @ $150
      const sellRes = await chai.request(server).post("/orders").send({
        symbol: "AAPL",
        side: "SELL",
        price: 150.0,
        quantity: 200,
      });

      sellRes.should.have.status(201);

      // 2. Post a BUY order: 50 shares @ $150
      const buyRes = await chai.request(server).post("/orders").send({
        symbol: "AAPL",
        side: "BUY",
        price: 150.0,
        quantity: 50,
      });
      buyRes.should.have.status(201);
      buyRes.body.status.should.eql("FILLED");
      buyRes.body.remainingQuantity.should.eql(0);

      // The original SELL order should now be PARTIALLY_FILLED with 150 remaining
      const updatedSell = await Order.findByPk(sellRes.body.id);
      should.exist(updatedSell);
      updatedSell.status.should.eql("PARTIALLY_FILLED");
      updatedSell.remainingQuantity.should.eql(150);
    });

    it("should execute matching with best price priority (lowest ask first)", async () => {
      // 1. Higher ask: SELL 100 @ 105
      const higherSell = await chai.request(server).post("/orders").send({
        symbol: "MSFT",
        side: "SELL",
        price: 105.0,
        quantity: 100,
      });
      higherSell.should.have.status(201);

      // 2. Lower ask: SELL 100 @ 100 (better price)
      const cheapSell = await chai.request(server).post("/orders").send({
        symbol: "MSFT",
        side: "SELL",
        price: 100.0,
        quantity: 100,
      });
      cheapSell.should.have.status(201);

      // 3. Incoming BUY: 100 @ 110 (crosses both, but must match cheapSell first)
      const buyRes = await chai.request(server).post("/orders").send({
        symbol: "MSFT",
        side: "BUY",
        price: 110.0,
        quantity: 100,
      });
      buyRes.should.have.status(201);
      buyRes.body.status.should.eql("FILLED");

      const refreshedCheap = await Order.findByPk(cheapSell.body.id);
      should.exist(refreshedCheap);
      refreshedCheap.status.should.eql("FILLED");
      refreshedCheap.remainingQuantity.should.eql(0);
    });
  });

  describe("DELETE /orders/:id - Order Cancellation Lifecycle", () => {
    it("should cancel an OPEN order with 200 OK", async () => {
      const order = await Order.create({
        symbol: "GS",
        side: "BUY",
        price: 200,
        quantity: 50,
        remainingQuantity: 50,
        status: "OPEN",
      });

      const res = await chai.request(server).delete(`/orders/${order.id}`);
      res.should.have.status(200);
      res.body.status.should.eql("CANCELLED");

      const dbOrder = await Order.findByPk(order.id);
      dbOrder.status.should.eql("CANCELLED");
    });

    it("should return 404 if order does not exist", async () => {
      const res = await chai.request(server).delete("/orders/99999");
      res.should.have.status(404);
    });

    it("should return 422 if attempting to cancel a FILLED order", async () => {
      const order = await Order.create({
        symbol: "GS",
        side: "BUY",
        price: 200,
        quantity: 50,
        remainingQuantity: 0,
        status: "FILLED",
      });

      const res = await chai.request(server).delete(`/orders/${order.id}`);
      res.should.have.status(422);
      res.body.should.have.property("error");
    });

    it("should return 400 if attempting to cancel an already CANCELLED order", async () => {
      const order = await Order.create({
        symbol: "GS",
        side: "BUY",
        price: 200,
        quantity: 50,
        remainingQuantity: 50,
        status: "CANCELLED",
      });

      const res = await chai.request(server).delete(`/orders/${order.id}`);
      res.should.have.status(400);
      res.body.should.have.property("error");
    });
  });

  describe("GET /orderbook/:symbol - Aggregated Depth", () => {
    it("should return aggregated and sorted bids (DESC) and asks (ASC) excluding FILLED/CANCELLED", async () => {
      await Order.bulkCreate([
        // Active Bids
        { symbol: "GS", side: "BUY", price: 300, quantity: 100, remainingQuantity: 100, status: "OPEN" },
        { symbol: "GS", side: "BUY", price: 300, quantity: 50, remainingQuantity: 50, status: "OPEN" },
        { symbol: "GS", side: "BUY", price: 295, quantity: 40, remainingQuantity: 40, status: "OPEN" },
        // Active Asks
        { symbol: "GS", side: "SELL", price: 305, quantity: 80, remainingQuantity: 80, status: "OPEN" },
        { symbol: "GS", side: "SELL", price: 310, quantity: 120, remainingQuantity: 120, status: "OPEN" },
        // Inactive (should be excluded)
        { symbol: "GS", side: "BUY", price: 302, quantity: 60, remainingQuantity: 0, status: "FILLED" },
        { symbol: "GS", side: "SELL", price: 303, quantity: 70, remainingQuantity: 70, status: "CANCELLED" },
      ]);

      const res = await chai.request(server).get("/orderbook/GS");
      res.should.have.status(200);
      res.body.symbol.should.eql("GS");

      // Bids sorted DESC by price
      res.body.bids.length.should.eql(2);
      res.body.bids[0].should.deep.eql({ price: 300, totalQuantity: 150 }); // 100 + 50
      res.body.bids[1].should.deep.eql({ price: 295, totalQuantity: 40 });

      // Asks sorted ASC by price
      res.body.asks.length.should.eql(2);
      res.body.asks[0].should.deep.eql({ price: 305, totalQuantity: 80 });
      res.body.asks[1].should.deep.eql({ price: 310, totalQuantity: 120 });
    });
  });

  describe("GET /orders - Order Listing & Filters", () => {
    it("should filter orders by symbol and status", async () => {
      await Order.bulkCreate([
        { symbol: "GS", side: "BUY", price: 100, quantity: 10, remainingQuantity: 10, status: "OPEN" },
        { symbol: "GS", side: "SELL", price: 100, quantity: 10, remainingQuantity: 0, status: "FILLED" },
        { symbol: "AAPL", side: "BUY", price: 150, quantity: 20, remainingQuantity: 20, status: "OPEN" },
      ]);

      const res = await chai.request(server).get("/orders?symbol=GS&status=OPEN");
      res.should.have.status(200);
      res.body.length.should.eql(1);
      res.body[0].symbol.should.eql("GS");
      res.body[0].status.should.eql("OPEN");
    });
  });
});
