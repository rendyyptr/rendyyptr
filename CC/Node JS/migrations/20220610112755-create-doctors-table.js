'use strict';

module.exports = {
  async up (queryInterface, Sequelize){
    await queryInterface.createTable('doctors',{
      id:{
        type: Sequelize.INTEGER,
        primaryKey : true,
        autoIncrement : true,
        allowNull : false
      },
      email:{
        type: Sequelize.STRING,
        unique: true,
        allowNull : false
      },
      name:{
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
    await queryInterface.dropTable('doctors')
  }
};
