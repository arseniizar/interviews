const express = require("express");
const router = express.Router();
const authController = require("../controllers/auth");

// POST /api/auth/register
router.post("/auth/register", authController.register);

// POST /api/auth/login
router.post("/auth/login", authController.login);

// GET /api/users/:id
router.get("/users/:id", authController.getUserById);

module.exports = router;
