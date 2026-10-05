const express = require("express");
const router = express.Router();
const ordersController = require("../controllers/orders");

// TODO: Connect routes to controller methods:
// POST   /orders           -> ordersController.createOrder
// DELETE /orders/:id       -> ordersController.cancelOrder
// GET    /orderbook/:symbol -> ordersController.getOrderBook
// GET    /orders           -> ordersController.getOrders

module.exports = router;
