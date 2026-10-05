# Challenge 1: Student Filter API (HackerRank Sample Clone)

This challenge is a 1-to-1 clone of the official Goldman Sachs HackerRank sample assessment (Node.js + Express + Sequelize + SQLite).

## Problem Description
Implement a REST service that exposes the `/students` endpoint. It should allow for filtering the collection of students as described below.

### Endpoint
`GET /students`

### Query Parameters
1. **`search`** (string, optional):
   - Filters the collection to return students whose `name` property contains the passed substring.
   - Sequelize hint: `name: { [Op.like]: '%' + search + '%' }`.
2. **`marksLow`** (number, optional):
   - Lower bound for student marks (exclusive: `marks > marksLow`).
3. **`marksHigh`** (number, optional):
   - Upper bound for student marks (exclusive: `marks < marksHigh`).

### Business Rules & Requirements
- **Boundary Validation:** If either `marksLow` or `marksHigh` is present without the other, respond with HTTP status **`400 Bad Request`**.
- **Marks Range Filtering:** When both `marksLow` and `marksHigh` are provided, return students who scored marks between the specified values (exclusive):
  - Sequelize hint: `[Op.and]: [{ marks: { [Op.gt]: Number(marksLow) } }, { marks: { [Op.lt]: Number(marksHigh) } }]`.
- **Combined Filtering:** Both `search` and marks filters can be applied together.
- **Sorting:** Results must be ordered by `id` ascending (`ASC`).
- **Success Response:** HTTP status **`200 OK`** returning a JSON array of matching student objects.

### Files to Edit
- [controllers/students.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task1_student_filtering/controllers/students.js)
- [routes/students.js](file:///Users/arseniizarudniuk/test/code_tasks_prep/goldman_sachs/node_task1_student_filtering/routes/students.js)

### Running Tests
```bash
python3 run_tests.py
# or
npm test
```
