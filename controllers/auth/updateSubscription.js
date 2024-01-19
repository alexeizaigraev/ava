const updateUser = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const { ctrlWrapper } = require("../../decorators");
const updateSubscription = async (req, res) => {
  const { id } = req.user;

  let result = await updateUser( { id }, { subscription: req.body } )
 
  if (!result) {
    throw HttpError(404, `Not found`);
  }

  res.json({ result });
};

module.exports = {
  updateSubscription: ctrlWrapper(updateSubscription),
};
