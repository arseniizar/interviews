const chai = require("chai");
const chaiHttp = require("chai-http");
const server = require("../app");
const Students = require("../models/students");
const connection = require("../connection");
const should = chai.should();

chai.use(chaiHttp);

describe("Students Filter API", () => {
  before(async () => {
    await connection.initialize();
  });

  after(async () => {
    await Students.drop();
  });

  it("Should get all the students", async () => {
    const response = await chai.request(server).get("/students");
    response.should.have.status(200);
    response.body.forEach((student, index) => {
      student.id.should.eql(index + 1);
      if (index === 0) {
        student.should.eql({
          id: 1,
          name: "Darcy Cherry",
          marks: 51.1,
        });
      }
    });
  });

  it("Should get all the students having the string `ra`", async () => {
    const response = await chai.request(server).get("/students?search=ra");
    response.should.have.status(200);
    response.body.length.should.eql(3);
    response.body.forEach((student, index) => {
      if (index === 0) {
        student.id.should.eql(5);
        student.name.should.eql("Bradshaw Cote");
        student.marks.should.eql(95);
      } else if (index === 1) {
        student.id.should.eql(15);
        student.name.should.eql("Brady Moss");
        student.marks.should.eql(17.4);
      } else if (index === 2) {
        student.id.should.eql(18);
        student.name.should.eql("Francisca Ewing");
        student.marks.should.eql(82.6);
      }
    });
  });

  it("should get all the students having the string `ra` and marks in between 85 and 100", async () => {
    const response = await chai
      .request(server)
      .get("/students?search=ra&marksLow=85&marksHigh=100");
    response.should.have.status(200);
    response.body.length.should.eql(1);
    response.body.forEach((student) => {
      student.id.should.eql(5);
      student.name.should.eql("Bradshaw Cote");
      student.marks.should.eql(95);
    });
  });

  it("should get all the students having marks in between 50 and 80", async () => {
    const response = await chai
      .request(server)
      .get("/students?marksLow=50&marksHigh=80");
    response.should.have.status(200);
    response.body.length.should.eql(9);
    response.body.forEach((student, index) => {
      if (index === 1) {
        student.id.should.eql(2);
        student.name.should.eql("Sanchez Woodward");
        student.marks.should.eql(53);
      } else if (index === 3) {
        student.id.should.eql(12);
        student.name.should.eql("Alissa Rowland");
        student.marks.should.eql(75.5);
      } else if (index === 6) {
        student.id.should.eql(21);
        student.name.should.eql("Angel Davis");
        student.marks.should.eql(73.5);
      }
    });
  });

  it("should respond with 400 if both marksLow and marksHigh are not present - 1", async () => {
    const response = await chai.request(server).get("/students?marksLow=30");
    response.should.have.status(400);
  });

  it("should respond with 400 if both marksLow and marksHigh are not present - 2", async () => {
    const response = await chai.request(server).get("/students?marksHigh=90");
    response.should.have.status(400);
  });
});
