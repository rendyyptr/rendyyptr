module.exports = (sequelize,DataTypes) =>{
    const PredictResult = sequelize.define('PredictResult',{
        id:{
            type: DataTypes.INTEGER,
            primaryKey : true,
            autoIncrement : true,
            allowNull : false
          },
          doctor_email:{
            type: DataTypes.STRING,
            allowNull : false
          },
          patient_email:{
            type: DataTypes.STRING,
            allowNull : false
          },
          image:{
            type:DataTypes.TEXT,
            allowNull : false
          },
          result:{
            type: DataTypes.STRING,
            allowNull : false
          },
          createdAt:{
            type:DataTypes.DATE,
            allowNull:false
          },
          updatedAt:{
            type:DataTypes.DATE,
            allowNull:false
          }
    },{
        tableName :'predict_results'
    });
    return PredictResult;
}