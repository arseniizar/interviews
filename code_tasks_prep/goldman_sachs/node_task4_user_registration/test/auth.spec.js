const chai = require("chai");
const chaiHttp = require("chai-http");
const server = require("../app");
const User = require("../models/user");
const connection = require("../connection");
const should = chai.should();

chai.use(chaiHttp);

describe("User Registration & Authentication API", () => {
  beforeEach(async () => {
    await connection.initialize();
  });

  after(async () => {
    await User.drop();
  });

  describe("POST /api/auth/register - Input Validation", () => {
    it("should return 400 if required fields are missing", async () => {
      const res = await chai.request(server).post("/api/auth/register").send({
        username: "testuser",
        // missing email & password
      });
      res.should.have.status(400);
      res.body.should.have.property("error");
    });

    it("should return 400 if username is invalid (less than 3 chars or non-alphanumeric)", async () => {
      const res1 = await chai.request(server).post("/api/auth/register").send({
        username: "ab",
        email: "valid@test.com",
        password: "Password123!",
      });
      res1.should.have.status(400);

      const res2 = await chai.request(server).post("/api/auth/register").send({
        username: "invalid user!",
        email: "valid@test.com",
        password: "Password123!",
      });
      res2.should.have.status(400);
    });

    it("should return 400 if email is malformed", async () => {
      const res = await chai.request(server).post("/api/auth/register").send({
        username: "johndoe",
        email: "not-an-email",
        password: "Password123!",
      });
      res.should.have.status(400);
    });

    it("should return 400 if password does not meet complexity (min 8 chars, uppercase, digit, special char)", async () => {
      // Missing special char
      const res1 = await chai.request(server).post("/api/auth/register").send({
        username: "johndoe",
        email: "john@example.com",
        password: "Password123",
      });
      res1.should.have.status(400);

      // Too short (< 8 chars)
      const res2 = await chai.request(server).post("/api/auth/register").send({
        username: "johndoe",
        email: "john@example.com",
        password: "Pass1!",
      });
      res2.should.have.status(400);

      // Missing uppercase
      const res3 = await chai.request(server).post("/api/auth/register").send({
        username: "johndoe",
        email: "john@example.com",
        password: "password123!",
      });
      res3.should.have.status(400);
    });
  });

  describe("POST /api/auth/register - Success & Conflict Handling", () => {
    it("should successfully register a user and return 201 without exposing the password", async () => {
      const res = await chai.request(server).post("/api/auth/register").send({
        username: "sarah_connor",
        email: "sarah@skynet.com",
        password: "StrongPassword123!",
      });

      res.should.have.status(201);
      res.body.should.have.property("id");
      res.body.username.should.eql("sarah_connor");
      res.body.email.should.eql("sarah@skynet.com");
      res.body.role.should.eql("USER");
      res.body.should.not.have.property("password");

      // Verify password was hashed in database
      const dbUser = await User.findByPk(res.body.id);
      should.exist(dbUser);
      dbUser.password.should.not.eql("StrongPassword123!");
    });

    it("should return 409 Conflict if username is already taken", async () => {
      await chai.request(server).post("/api/auth/register").send({
        username: "alex99",
        email: "alex1@test.com",
        password: "Password123!",
      });

      const res = await chai.request(server).post("/api/auth/register").send({
        username: "alex99", // duplicate
        email: "alex2@test.com",
        password: "Password123!",
      });

      res.should.have.status(409);
      res.body.error.should.match(/username/i);
    });

    it("should return 409 Conflict if email is already in use", async () => {
      await chai.request(server).post("/api/auth/register").send({
        username: "user_one",
        email: "shared@test.com",
        password: "Password123!",
      });

      const res = await chai.request(server).post("/api/auth/register").send({
        username: "user_two",
        email: "shared@test.com", // duplicate
        password: "Password123!",
      });

      res.should.have.status(409);
      res.body.error.should.match(/email/i);
    });
  });

  describe("POST /api/auth/login - Authentication", () => {
    beforeEach(async () => {
      // Register a standard user
      await chai.request(server).post("/api/auth/register").send({
        username: "alice",
        email: "alice@test.com",
        password: "MySecurePassword1!",
      });
    });

    it("should successfully authenticate with valid credentials", async () => {
      const res = await chai.request(server).post("/api/auth/login").send({
        username: "alice",
        password: "MySecurePassword1!",
      });

      res.should.have.status(200);
      res.body.should.have.property("user");
      res.body.user.username.should.eql("alice");
      res.body.user.should.not.have.property("password");
    });

    it("should return 401 Unauthorized for incorrect password", async () => {
      const res = await chai.request(server).post("/api/auth/login").send({
        username: "alice",
        password: "WrongPassword999!",
      });

      res.should.have.status(401);
      res.body.should.have.property("error");
    });

    it("should return 401 Unauthorized for non-existent user", async () => {
      const res = await chai.request(server).post("/api/auth/login").send({
        username: "ghost_user",
        password: "MySecurePassword1!",
      });

      res.should.have.status(401);
      res.body.should.have.property("error");
    });
  });

  describe("GET /api/users/:id - User Profile", () => {
    it("should return 200 with user profile excluding password", async () => {
      const reg = await chai.request(server).post("/api/auth/register").send({
        username: "bob_ross",
        email: "bob@canvas.com",
        password: "HappyTrees123!",
      });

      const res = await chai.request(server).get(`/api/users/${reg.body.id}`);
      res.should.have.status(200);
      res.body.username.should.eql("bob_ross");
      res.body.email.should.eql("bob@canvas.com");
      res.body.should.not.have.property("password");
    });

    it("should return 404 if user not found", async () => {
      const res = await chai.request(server).get("/api/users/9999");
      res.should.have.status(404);
    });
  });
});
