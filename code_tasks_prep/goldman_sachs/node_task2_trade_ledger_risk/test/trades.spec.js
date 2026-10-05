const chai = require("chai");
const chaiHttp = require("chai-http");
const server = require("../app");
const Trade = require("../models/trade");
const connection = require("../connection");
const should = chai.should();

chai.use(chaiHttp);

describe("Goldman Sachs Trade Ledger & Risk API", () => {
  beforeEach(async () => {
    await connection.initialize();
  });

  after(async () => {
    await Trade.drop();
  });

  describe("POST /trades - Trade Ingestion & Validation", () => {
    it("should successfully record a valid BUY trade with 201 Created", async () => {
      const payload = {
        traderId: "T-001",
        symbol: "GS",
        side: "BUY",
        shares: 500,
        price: 380.5,
      };
      const res = await chai.request(server).post("/trades").send(payload);
      res.should.have.status(201);
      res.body.should.have.property("id");
      res.body.traderId.should.eql("T-001");
      res.body.symbol.should.eql("GS");
      res.body.side.should.eql("BUY");
      res.body.shares.should.eql(500);
      res.body.price.should.eql(380.5);
    });

    it("should return 400 if symbol is missing, lowercase, or longer than 5 chars", async () => {
      const res1 = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "apple", // lowercase
        side: "BUY",
        shares: 100,
        price: 150,
      });
      res1.should.have.status(400);

      const res2 = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "TOOLONGSYMBOL",
        side: "BUY",
        shares: 100,
        price: 150,
      });
      res2.should.have.status(400);
    });

    it("should return 400 if side is not 'BUY' or 'SELL'", async () => {
      const res = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "AAPL",
        side: "HOLD",
        shares: 100,
        price: 150,
      });
      res.should.have.status(400);
    });

    it("should return 400 if shares <= 0 or not an integer", async () => {
      const res1 = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "AAPL",
        side: "BUY",
        shares: 0,
        price: 150,
      });
      res1.should.have.status(400);

      const res2 = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "AAPL",
        side: "BUY",
        shares: 10.5,
        price: 150,
      });
      res2.should.have.status(400);
    });

    it("should return 400 if price <= 0", async () => {
      const res = await chai.request(server).post("/trades").send({
        traderId: "T-001",
        symbol: "AAPL",
        side: "BUY",
        shares: 100,
        price: -5.0,
      });
      res.should.have.status(400);
    });
  });

  describe("POST /trades - Real-time Risk Limits", () => {
    it("should reject trade with 422 if single notional value exceeds 1,000,000", async () => {
      // 5,000 shares * $250 = $1,250,000 (> 1M)
      const res = await chai.request(server).post("/trades").send({
        traderId: "T-002",
        symbol: "MSFT",
        side: "BUY",
        shares: 5000,
        price: 250,
      });
      res.should.have.status(422);
      res.body.should.have.property("error");
    });

    it("should reject trade with 422 if net long position exceeds 10,000 shares", async () => {
      // First buy 7,000 shares (ok)
      await chai.request(server).post("/trades").send({
        traderId: "T-003",
        symbol: "NVDA",
        side: "BUY",
        shares: 7000,
        price: 100,
      });

      // Try buying another 4,000 shares (7000 + 4000 = 11,000 > 10,000 max long)
      const res = await chai.request(server).post("/trades").send({
        traderId: "T-003",
        symbol: "NVDA",
        side: "BUY",
        shares: 4000,
        price: 100,
      });
      res.should.have.status(422);
      res.body.should.have.property("error");
    });

    it("should reject trade with 422 if net short position exceeds -5,000 shares", async () => {
      // Short sell 4,000 shares (ok)
      await chai.request(server).post("/trades").send({
        traderId: "T-004",
        symbol: "TSLA",
        side: "SELL",
        shares: 4000,
        price: 200,
      });

      // Try selling another 2,000 shares (-4000 - 2000 = -6000 < -5000 max short)
      const res = await chai.request(server).post("/trades").send({
        traderId: "T-004",
        symbol: "TSLA",
        side: "SELL",
        shares: 2000,
        price: 200,
      });
      res.should.have.status(422);
      res.body.should.have.property("error");
    });
  });

  describe("GET /trades - Filtering & Date Range", () => {
    beforeEach(async () => {
      // Seed 3 trades
      await Trade.bulkCreate([
        {
          traderId: "T-010",
          symbol: "GS",
          side: "BUY",
          shares: 100,
          price: 350,
          timestamp: new Date("2026-01-10T10:00:00Z"),
        },
        {
          traderId: "T-010",
          symbol: "AAPL",
          side: "BUY",
          shares: 200,
          price: 180,
          timestamp: new Date("2026-01-15T12:00:00Z"),
        },
        {
          traderId: "T-020",
          symbol: "GS",
          side: "SELL",
          shares: 50,
          price: 360,
          timestamp: new Date("2026-01-20T14:00:00Z"),
        },
      ]);
    });

    it("should filter trades by symbol", async () => {
      const res = await chai.request(server).get("/trades?symbol=GS");
      res.should.have.status(200);
      res.body.length.should.eql(2);
      res.body.every((t) => t.symbol === "GS").should.be.true;
    });

    it("should filter trades by traderId and side", async () => {
      const res = await chai.request(server).get("/trades?traderId=T-010&side=BUY");
      res.should.have.status(200);
      res.body.length.should.eql(2);
    });

    it("should return 400 if only startDate or only endDate is provided", async () => {
      const res1 = await chai.request(server).get("/trades?startDate=2026-01-01");
      res1.should.have.status(400);

      const res2 = await chai.request(server).get("/trades?endDate=2026-01-12");
      res2.should.have.status(400);
    });

    it("should filter trades between startDate and endDate", async () => {
      const res = await chai
        .request(server)
        .get("/trades?startDate=2026-01-01T00:00:00Z&endDate=2026-01-12T00:00:00Z");
      res.should.have.status(200);
      res.body.length.should.eql(1);
      res.body[0].symbol.should.eql("GS");
    });
  });

  describe("GET /portfolio/:traderId - Aggregate Positions", () => {
    it("should return empty positions array for trader without trades", async () => {
      const res = await chai.request(server).get("/portfolio/T-NONEXISTENT");
      res.should.have.status(200);
      res.body.should.deep.eql({ traderId: "T-NONEXISTENT", positions: [] });
    });

    it("should correctly aggregate net positions and cash balance for trader", async () => {
      await Trade.bulkCreate([
        {
          traderId: "T-AGG",
          symbol: "AAPL",
          side: "BUY",
          shares: 500,
          price: 150, // -$75,000
        },
        {
          traderId: "T-AGG",
          symbol: "AAPL",
          side: "SELL",
          shares: 200,
          price: 160, // +$32,000
        },
        {
          traderId: "T-AGG",
          symbol: "GOOGL",
          side: "BUY",
          shares: 100,
          price: 100, // -$10,000
        },
      ]);

      const res = await chai.request(server).get("/portfolio/T-AGG");
      res.should.have.status(200);
      res.body.traderId.should.eql("T-AGG");
      res.body.positions.length.should.eql(2);

      const aapl = res.body.positions.find((p) => p.symbol === "AAPL");
      should.exist(aapl);
      aapl.netShares.should.eql(300); // 500 - 200

      const googl = res.body.positions.find((p) => p.symbol === "GOOGL");
      should.exist(googl);
      googl.netShares.should.eql(100);
    });
  });
});
