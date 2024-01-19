const updateUser = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");
const { SECRET_KEY } = process.env;


const login = async (req, res) => {
  // const { email, password } = req.body
  const email = req.body.email
  const password = req.body.password
  console.log("req.body=", req.body)

  if (!email || !password) {
    throw HttpError(400, "Email or password is missing");
  }

  console.log("email:", email)
  let user = await getUser({email})
  
  console.log("find by email user=", user)
  if (!user) {
    throw HttpError(401, "Email or password is wrong");
  }

  // console.log('password, user.password =', password, user.password)
  const passwordCompare = await bcrypt.compare(password, user.password);
  if (!passwordCompare) {
    throw HttpError(401, "Email or password is wrong");
  }

  const payload = {
    id: user.id,
  };
  // console.log("payload", payload)
  const token = jwt.sign(payload, SECRET_KEY, { expiresIn: "230h" });
  // console.log('token=', token)

  const q = `
  UPDATE users
  SET
    token = $2
  WHERE id = $1
  RETURNING *`
  
  
  let result = await updateUser({email}, {token})

  res.json({
    token: token,
    user: {
      name: user.name,
      email: user.email,
      subscription: user.subscription,
      status: user.status, 
      avatarUrl: user.avatarurl,
    },
  });
};
module.exports = {
  login: ctrlWrapper(login),
};
