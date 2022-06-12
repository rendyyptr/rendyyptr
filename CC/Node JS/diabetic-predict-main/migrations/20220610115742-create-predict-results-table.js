'use strict';

module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.createTable('predict_results',{
      id:{
        type: Sequelize.INTEGER,
        primaryKey : true,
        autoIncrement : true,
        allowNull : false
      },
      doctor_email:{
        type: Sequelize.STRING,
        allowNull : false,
        defaultValue:"Not Set"
      },
      patient_email:{
        type: Sequelize.STRING,
        allowNull : false,
        defaultValue:"Not Set"
      },
      image:{
        type:Sequelize.TEXT,
        allowNull : false
      },
      result:{
        type: Sequelize.STRING,
        allowNull : false
      },
      createdAt:{
        type:Sequelize.DATE,
        allowNull:false,
        defaultValue: Sequelize.fn('NOW')
      },
      updatedAt:{
        type:Sequelize.DATE,
        allowNull:false,
        defaultValue: Sequelize.fn('NOW')
      }
    });
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.dropTable('predict_results');
  }
};
