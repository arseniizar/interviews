const router = require("express").Router();
const studentsController = require("../controllers/students");

// TODO: Connect route to controller method: GET / -> studentsController.getStudents
router.get("/", studentsController.getStudents);

module.exports = router;
