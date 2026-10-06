const express = require("express");
const authRouter = require("./routes/auth");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Mount all auth routes under /api
app.use("/api", authRouter);

module.exports = app;
