const Students = require("../models/students");
const { Op } = require("sequelize");

// TODO: Implement getStudents from scratch.
//
// Requirements:
// 1. Accepts query parameters: search, marksLow, marksHigh.
// 2. If either marksLow or marksHigh is present without the other -> return HTTP 400 Bad Request.
// 3. If search is provided -> filter name by substring: { [Op.like]: `%${search}%` }.
// 4. If marksLow and marksHigh are provided -> filter marks: { [Op.gt]: Number(marksLow), [Op.lt]: Number(marksHigh) }.
// 5. Order results by id ASC.
// 6. Return HTTP 200 OK with array of matching students.

module.exports = {};
