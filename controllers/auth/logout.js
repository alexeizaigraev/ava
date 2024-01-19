// logout
const updateUser = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const { ctrlWrapper } = require("../../decorators");

const logout = async (req, res) => {
  const id = req.user.id
  await updateUser({id}, {token: null})
  
  res.status(204).json({
    message: "Logout success",
  });
};
module.exports = {
  logout: ctrlWrapper(logout),
};
