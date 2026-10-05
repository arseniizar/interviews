const fixtureData = require("./fixtures/data.json");
const Students = require("./models/students");

module.exports = {
  load: async () => {
    const rows = fixtureData.map((entry) => entry.data);
    await Students.bulkCreate(rows);
  },
};
