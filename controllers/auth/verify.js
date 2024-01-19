const updateUserPrisma = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')


const { ctrlWrapper } = require("../../decorators");
const { HttpError } = require("../../helpers");
const updateUser = require('./updateUser');

const verify = async (req, res) => {
  const { verificationtoken } = req.params;
  console.log('verificationtoken= ', verificationtoken)

  let user = await getUser({verificationtoken})
  
  if (!user) {
    throw HttpError(404, "User not found");
  }

  let result = updateUser( {id: user.id}, {verificationtoken: true} )
  
  console.log('result=', result)
  res.json({
    
    message: `Верификация прошла успешно. Зайдите в приложение под своим логином и паролем. Логин: "${user.email}"    `
    
 
  });
};

module.exports = {
  verify: ctrlWrapper(verify),
};
