const User = require("../models/user");
const crypto = require("crypto");

/**
 * Helper to hash password using sha256 (Node built-in crypto)
 */
const hashPassword = (password) => {
  return crypto.createHash("sha256").update(password).digest("hex");
};

/**
 * Helper to validate email format
 */
const isValidEmail = (email) => {
  return typeof email === "string" && email.includes("@") && email.includes(".");
};

/**
 * Helper to validate password complexity:
 * - At least 8 characters
 * - At least one uppercase letter ([A-Z])
 * - At least one digit ([0-9])
 * - At least one special character ([!@#$%^&*])
 */
const isValidPassword = (password) => {
  if (typeof password !== "string" || password.length < 8) return false;
  const hasUpper = /[A-Z]/.test(password);
  const hasDigit = /[0-9]/.test(password);
  const hasSpecial = /[!@#$%^&*]/.test(password);
  return hasUpper && hasDigit && hasSpecial;
};

/**
 * Helper to validate username:
 * - 3 to 20 alphanumeric characters only (letters, numbers, underscore)
 */
const isValidUsername = (username) => {
  return typeof username === "string" && /^[a-zA-Z0-9_]{3,20}$/.test(username);
};

// TODO: Implement the controller methods from scratch:

/**
 * POST /api/auth/register
 * Body: { username, email, password, role }
 *
 * Rules:
 * 1. Validation (HTTP 400 Bad Request):
 *    - Check isValidUsername(username)
 *    - Check isValidEmail(email)
 *    - Check isValidPassword(password)
 *    - If invalid -> return res.status(400).json({ error: "Invalid registration details" })
 *
 * 2. Uniqueness / Conflict (HTTP 409 Conflict):
 *    - Check if User already exists with username -> return 409 { error: "Username already taken" }
 *    - Check if User already exists with email -> return 409 { error: "Email already in use" }
 *
 * 3. Creation (HTTP 201 Created):
 *    - Hash password: hashPassword(password)
 *    - Create user in DB
 *    - Return user object EXCLUDING the password field!
 */
const register = async (req, res) => {
  res.status(501).json({ message: "Not implemented yet" });
};

/**
 * POST /api/auth/login
 * Body: { username, password }
 *
 * Rules:
 * 1. If username or password missing -> 400 Bad Request { error: "Username and password required" }
 * 2. Find user by username
 * 3. If user doesn't exist OR hashPassword(password) !== user.password:
 *    -> return 401 Unauthorized { error: "Invalid credentials" }
 * 4. Return 200 OK:
 *    {
 *      message: "Login successful",
 *      user: { id, username, email, role }
 *    }
 */
const login = async (req, res) => {
  res.status(501).json({ message: "Not implemented yet" });
};

/**
 * GET /api/users/:id
 * Path param: id
 *
 * Rules:
 * 1. Find user by pk
 * 2. If not found -> 404 Not Found { error: "User not found" }
 * 3. Return 200 OK with user object (EXCLUDING password field)
 */
const getUserById = async (req, res) => {
  res.status(501).json({ message: "Not implemented yet" });
};

module.exports = {
  register,
  login,
  getUserById,
  hashPassword,
  isValidEmail,
  isValidPassword,
  isValidUsername,
};
