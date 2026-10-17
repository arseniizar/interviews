const Trade = require("../models/trade");
const { Op } = require("sequelize");

// Risk Limits:
// 1. Single transaction: (shares * price) <= 1,000,000
//    (otherwise 422: "Order value exceeds single transaction limit of 1,000,000")
// 2. Net position limit per symbol:
//    - Max long: 10,000 shares (otherwise 422: "Maximum long position limit of 10,000 shares exceeded")
//    - Max short: -5,000 shares (otherwise 422: "Maximum short position limit of -5,000 shares exceeded")

/**
 * POST /trades
 * 1. Validation (HTTP 400 Bad Request):
 *    - traderId: non-empty string
 *    - symbol: uppercase string, length 1..5
 *    - side: strictly 'BUY' or 'SELL'
 *    - shares: integer > 0 (Number.isInteger(shares) && shares > 0)
 *    - price: number > 0 (typeof price === 'number' && price > 0)
 * 2. Risk Checks (HTTP 422 Unprocessable Entity):
 *    - Single transaction: shares * price <= 1,000,000
 *      error: "Order value exceeds single transaction limit of 1,000,000"
 *    - Net position limit per symbol for this trader:
 *      currentNet = sum(BUY shares) - sum(SELL shares) of existing trades for (traderId, symbol)
 *      proposedNet = currentNet + (side === 'BUY' ? shares : -shares)
 *      if proposedNet > 10000: error: "Maximum long position limit of 10,000 shares exceeded"
 *      if proposedNet < -5000: error: "Maximum short position limit of -5,000 shares exceeded"
 * 3. Save:
 *    - Trade.create({ traderId, symbol, side, shares, price }) -> status 201 with created trade
 */
const createTrade = async (req, res) => {
  const { traderId, symbol, side, shares, price } = req.body;

  if (!traderId || !symbol || !side || !shares || !price) {
    return res.status(400).json({ error: "invalid request body" });
  }

  if (typeof traderId !== "string" || traderId.length === 0) {
    return res.status(400).json({ error: "invalid request body" });
  }

  if (typeof side !== "string" || (side !== "BUY" && side !== "SELL")) {
    return res.status(400).json({ error: "invalid request body" });
  }

  if (!Number.isInteger(shares) || shares <= 0) {
    return res.status(400).json({ error: "invalid request body" });
  }

  if (typeof price !== "number" || price <= 0) {
    return res.status(400).json({ error: "invalid request body" });
  }

  if (shares * price > 1000000) {
    return res.status(422).json({ error: "Order value exceeds single transaction limit of 1,000,000" });
  }

  if (typeof symbol !== "string" || symbol !== symbol.toUpperCase() || symbol.length > 5 || symbol.length < 1) {
    return res.status(400).json({ error: "invalid request body" });
  }

  const existingTrades = await Trade.findAll({ where: { traderId, symbol } });

  let currentNet = 0;

  for (const t of existingTrades) {
    if (t.side === 'BUY') {
      currentNet += t.shares;
    } else {
      currentNet -= t.shares;
    }
  }

  let proposedNet = 0;

  if (side === "BUY") {
    proposedNet = currentNet + shares;
    if (proposedNet > 10000) {
      return res.status(422).json({ error: "Maximum long position limit of 10,000 shares exceeded" });
    }
  } else if (side === "SELL") {
    proposedNet = currentNet - shares;
    if (proposedNet < -5000) {
      return res.status(422).json({ error: "Maximum short position limit of -5,000 shares exceeded" });
    }
  }

  const trade = await Trade.create({ traderId, symbol, side, shares, price });

  return res.status(201).json(trade);
};

/**
 * GET /trades
 * Query params: traderId, symbol, side, startDate, endDate
 * 1. If only startDate or only endDate is provided -> status 400
 * 2. If both dates provided -> timestamp between startDate and endDate (Op.gte, Op.lte)
 * 3. Filter by traderId, symbol, side if provided
 * 4. Sort: order: [['timestamp', 'DESC']]
 * 5. Return status 200 with array
 */
const getTrades = async (req, res) => {
  const { traderId, symbol, side, startDate, endDate } = req.query;

  if ((startDate && !endDate) || (!startDate && endDate)) {
    return res.status(400).json({ error: "invalid request body" });
  }

  const where = {};
  const order = [['timestamp', 'DESC']];

  if (startDate && endDate) {
    where.timestamp = { [Op.gte]: startDate, [Op.lte]: endDate };
  }

  if (traderId) {
    where.traderId = traderId;
  }

  if (symbol) {
    where.symbol = symbol;
  }

  if (side) {
    where.side = side;
  }

  const trades = await Trade.findAll({ where, order });

  return res.status(200).json(trades);
};

/**
 * GET /portfolio/:traderId
 * 1. Find all trades where traderId === req.params.traderId
 * 2. Group / aggregate by symbol:
 *    netShares = sum(BUY shares) - sum(SELL shares)
 * 3. Return status 200 with { traderId, positions: [{ symbol, netShares }, ...] }
 */
const getPortfolio = async (req, res) => {
  const { traderId } = req.params;
  const trades = await Trade.findAll({ where: { traderId } });

  const group = {};

  for (const t of trades) {
    if (!group[t.symbol]) {
      group[t.symbol] = 0;
    }

    if (t.side === "BUY") {
      group[t.symbol] += t.shares;
    } else {
      group[t.symbol] -= t.shares;
    }
  }

  const positions = Object.keys(group).map((symbol) => ({
    symbol,
    netShares: group[symbol]
  }))

  return res.status(200).json({
    traderId,
    positions
  });
};

module.exports = {
  createTrade,
  getTrades,
  getPortfolio,
};

