module.exports = (sequelize,DataTypes)=>{
  const Doctor = sequelize.define('Doctor',{
        id:{
          type: DataTypes.INTEGER,
          primaryKey : true,
          autoIncrement : true,
          allowNull : false
        },
        email:{
          type: DataTypes.STRING,
          unique: true,
          allowNull : false
        },
        name:{
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
      tableName:'doctors'
  });
  return Doctor;
}