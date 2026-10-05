const Trade = require("../models/trade");
const { Op } = require("sequelize");

// Risk Limits:
// 1. Single transaction: (shares * price) <= 1,000,000
//    (otherwise 422: "Order value exceeds single transaction limit of 1,000,000")
// 2. Net position limit per symbol:
//    - Max long: 10,000 shares (otherwise 422: "Maximum long position limit of 10,000 shares exceeded")
//    - Max short: -5,000 shares (otherwise 422: "Maximum short position limit of -5,000 shares exceeded")

// TODO: Implement controller methods from scratch:
// 1. createTrade(req, res)
//    - Validation (400):
//      - traderId: non-empty string
//      - symbol: 1-5 uppercase letters
//      - side: 'BUY' or 'SELL'
//      - shares: integer > 0
//      - price: number > 0
//    - Risk checks (422)
//    - Save to DB -> status 201 with trade object
//
// 2. getTrades(req, res)
//    - Query: traderId, symbol, side, startDate, endDate
//    - If only startDate or only endDate is provided -> status 400
//    - Sort: timestamp DESC -> status 200
//
// 3. getPortfolio(req, res)
//    - Path: traderId
//    - Aggregation: calculate netShares for each symbol
//    - Response: { traderId, positions: [{ symbol, netShares }] } -> status 200

module.exports = {};
