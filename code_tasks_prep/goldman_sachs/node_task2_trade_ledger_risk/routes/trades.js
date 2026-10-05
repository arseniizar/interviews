const express = require("express");
const router = express.Router();
const tradesController = require("../controllers/trades");

// TODO: Connect routes to controller methods:
// POST /trades           -> tradesController.createTrade
// GET /trades            -> tradesController.getTrades
// GET /portfolio/:traderId -> tradesController.getPortfolio

module.exports = router;
