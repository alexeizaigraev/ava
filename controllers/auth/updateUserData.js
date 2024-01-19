const updateUserPrisma = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const { HttpError } = require("../../helpers");
// const { cloudinary } = require("../../cloudinary");
const { ctrlWrapper } = require("../../decorators");
const { parseConnectionUrl } = require("nodemailer/lib/shared");
const updateUser = require('./updateUser');


const updateUserData = async (req, res) => {
  console.log("req.params=", req.params)
  
  const id = req.params.id
  
  let { body } = req;
  // let bodyDtoIn = dtoUserIn(body)
  console.log("body=", body)
  let user = await getUser( {id} )
  
  if (!user) {
    throw HttpError(401, "User not find");
  }
  let name = body.hasOwnProperty("name") ? body.name : user.name
  let subscription = body.hasOwnProperty("subscription") ? body.subscription : user.subscription
      
  let result = await updateUser({id}, body)
  
  if (!result) {
    throw HttpError(404, `Not found`);
  }
  res.json(result);
};

module.exports = {
    updateUserData: ctrlWrapper(updateUserData),
};