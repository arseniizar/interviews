const Order = require("../models/order");
const { Op } = require("sequelize");

// TODO: Implement Limit Order Book & Matching Engine logic from scratch:
//
// 1. createOrder(req, res):
//    - Validation (400):
//      - symbol: non-empty string, 1-5 uppercase characters
//      - side: 'BUY' or 'SELL'
//      - price: number > 0
//      - quantity: integer > 0
//    - Matching Engine (Price-Time Priority):
//      - BUY matches against active SELL orders (status IN ('OPEN', 'PARTIALLY_FILLED')), where ask.price <= buy.price, lowest price first (price ASC, createdAt ASC).
//      - SELL matches against active BUY orders, where bid.price >= sell.price, highest price first (price DESC, createdAt ASC).
//      - Execute matchQty = Math.min(...) while quantity remains. Update opposite order statuses (FILLED or PARTIALLY_FILLED).
//    - Save created order with status ('OPEN', 'PARTIALLY_FILLED', or 'FILLED') -> status 201 Created.
//
// 2. cancelOrder(req, res):
//    - If not found -> 404 Not Found
//    - If already 'FILLED' -> 422: { error: "Cannot cancel completely filled order" }
//    - If already 'CANCELLED' -> 400: { error: "Order already cancelled" }
//    - If 'OPEN' or 'PARTIALLY_FILLED' -> update status to 'CANCELLED', return 200 OK.
//
// 3. getOrderBook(req, res):
//    - Return active market depth:
//      {
//        symbol: "...",
//        bids: [{ price, totalQuantity }], // sorted DESC by price
//        asks: [{ price, totalQuantity }]  // sorted ASC by price
//      }
//
// 4. getOrders(req, res):
//    - Filters: symbol, status. Sort: createdAt DESC -> 200 OK.

module.exports = {};
