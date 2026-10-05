const express = require("express");
const tradesRouter = require("./routes/trades");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/", tradesRouter);

module.exports = app;
