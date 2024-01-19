const createUser = require('../../prisma.methods/user/createUser')

const dtoUserIn = require('../../utils/dtoUserIn')
const dtoUserOut = require('../../utils/dtoUserOut')

const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const { randomUUID } = require("crypto");

const { HttpError, sendEmail } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");


const path = require("path");
const fs = require("fs/promises");
const gravatar = require("gravatar");
// import "dotenv/config";
//______________


const { SECRET_KEY, BASE_URL } = process.env;

const register = async (req, res) => {
  const { email, password, subscription } = req.body;
  // const candidate = await db.users.findByEmail(email)
  // if (candidate) {
  //   throw HttpError(409, "Email already in use");
  // }
  
  const hashPassword = await bcrypt.hash(password, 10);
  const avatarUrl = gravatar.url(email);
  const verificationToken = randomUUID();
  
  let user = {
    ...req.body
  }
  
  user.password = hashPassword
  user.avatarurl = avatarUrl
  user.verificationtoken = verificationToken
  user.verify = true
  user.status = "user"
  // const user = {
  //   email,
  //   hashPassword,
  //   avatarUrl,
  //   verificationToken,
  //   verify: true,
  //   status: "admin"
  // }
  console.log(user)
  const result = await createUser(user)

  console.log(result)
  const link = `${BASE_URL}/api/auth/verify/${verificationToken}`
  console.log(link)
  // console.log(BASE_URL, verificationToken);
  const verifyEmail = {
    to: email,
    subject: "Сonfirm your registration",
    html: `<a target="_blank" href="${BASE_URL}/api/auth/verify/${verificationToken}">Вас приветствует ТОВ Довира.  Click to confirm your registration</a>`,
  };

  //await sendEmail(verifyEmail);
  let outObj = {
    email: email,
    hashPassword: hashPassword,
    subscription: subscription,
    avatarurl: avatarUrl,
    verificationToken: verificationToken,
    status: user.statis
  }
  
  // let outObjDto = dtoUserOut(outObj)
  
  res.status(201).json(result);


};

module.exports = {
  register: ctrlWrapper(register),
};
