const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("sqlite::memory:", {
  logging: false,
});

module.exports = {
  sequelize,
  initialize: async () => {
    await sequelize.sync({ force: true });
  },
};
