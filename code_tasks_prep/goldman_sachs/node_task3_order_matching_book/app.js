const express = require("express");
const ordersRouter = require("./routes/orders");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/", ordersRouter);

module.exports = app;
