let jwt = require('jwt-simple');

module.exports = (req,res,next) =>{

    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];

    if(token == null) return res.sendStatus(401);

    try{
        let data = jwt.decode(token, process.env.JWT_SECRET,'RS256')
        if(data.iss !== process.env.ISS) return res.sendStatus(401);
        req.email = data.email;
        next();
    }catch(err){
        return res.sendStatus(400);
    }
}