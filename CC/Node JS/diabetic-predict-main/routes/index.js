var express = require('express');
var router = express.Router();
const {Doctor,PredictResult} = require('../models');
const Validator = require('fastest-validator');
const { json } = require('express/lib/response');
const v = new Validator();

router.post('/',async (req, res) => {
    try {
      const doctor = await Doctor.findOne({
        where: {
          email: req.email
        }
      });   
    if(doctor!=null){
        const result = await PredictResult.findAll({
            where:{
                doctor_email:req.email
            }
        });
        if(result !=null){
            return res.json({
                doctor:doctor.name,
                predict_results: result
            });
        }else{
            res.json({
                doctor:doctor.name,
                predict_results: "no_data"
            });
        }
    }else{
        const result = await PredictResult.findAll({
            where:{
                patient_email:req.email
            }
        });
        if(result !=null){
            return res.json({
                user : "patient",
                predict_results: result
            });
        }else{
            res.json({
                user : "patient",
                predict_results: "no_data"
            });
        }
    }
    } catch (error) {
      res.sendStatus(500);
    }
});

router.post('/result',async (req, res) => {
    const schema = {
        id: "string"
    }

    const validate = v.validate(req.body,schema);

    if(validate.length){
        return res
        .status(400)
        .json(validate);
    }

    try {
        const doctor = await Doctor.findOne({
          where: {
            email: req.email
          }
        });   
      if(doctor!=null){
          const result = await PredictResult.findOne({
              where: {
                doctor_email: req.email,
                id : req.body.id
              }
            });   
          if(result !=null){
              return res.json(result);
          }else{
              return res.sendStatus(404);
          }
      }else{
          const result = await PredictResult.findOne({
              where: {
                patient_email: req.email,
                id : req.body.id
              }
            });   
          if(result !=null){
              return res.json(result);
          }else{
              return res.sendStatus(404);
          }
      }
    } catch (error) {
      res.sendStatus(500);
    }
});

router.post('/predict',async (req, res) => {
    const schema = {
        image: "string",
        result: "string"
    }

    const validate = v.validate(req.body,schema);

    if(validate.length){
        return res
        .status(400)
        .json(validate);
    }

    try {
      const doctor = await Doctor.findOne({
        where: {
          email: req.email
        }
      });   
    if(doctor!=null){
        const result = await PredictResult.create({
           doctor_email:req.email,
           patient_email : "Not Set",
           image : req.body.image,
           result : req.body.result
        });
        res.json(result);
    }else{
        const result = await PredictResult.create({
            patient_email:req.email,
            doctor_email : "Not Set",
            image : req.body.image,
            result : "diabetic"
         });
         res.json(result);
    }
    } catch (error) {
      res.sendStatus(500);
    }
});

router.put('/predict',async (req, res) => {
    const schema = {
        id: "string",
        patient_email: "string"
    }

    const validate = v.validate(req.body,schema);

    if(validate.length){
        return res
        .status(400)
        .json(validate);
    }

    try {
      const doctor = await Doctor.findOne({
        where: {
          email: req.email
        }
      });   
    if(doctor!=null){
        const result = await PredictResult.update({
           patient_email : req.body.patient_email
        },{
            where:{
                id:req.body.id,
                doctor_email : req.email
        }});
        result ? res.json({message:"success update data"}):res.json({message:"failed update data"}).status(400);
    }else{
       res.sendStatus(401);
    }
    } catch (error) {
      res.sendStatus(500);
    }
});
module.exports = router;

