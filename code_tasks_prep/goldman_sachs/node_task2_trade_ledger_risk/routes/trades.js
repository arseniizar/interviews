const express = require("express");
const router = express.Router();
const tradesController = require("../controllers/trades");

router.post("/trades", tradesController.createTrade);
router.get("/trades", tradesController.getTrades);
router.get("/portfolio/:traderId", tradesController.getPortfolio);

module.exports = router;

