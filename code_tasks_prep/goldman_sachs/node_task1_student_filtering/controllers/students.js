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

const getStudents = async (req, res) => {
    try {
        const { search, marksLow, marksHigh } = req.query;

        if ((marksLow && !marksHigh) || (!marksLow && marksHigh)) {
            return res.status(400).send();
        }

        const where = {};

        if (search) {
            where.name = { [Op.like]: `%${search}%` }
        }

        if (marksLow && marksHigh) {
            where.marks = {
                [Op.gt]: Number(marksLow),
                [Op.lt]: Number(marksHigh)
            }
        }

        const students = await Students.findAll({
            where,
            order: [['id', 'ASC']]
        })

        return res.status(200).json(students)
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
}

module.exports = { getStudents };
