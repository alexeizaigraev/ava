const updateContact = require('../../prisma.methods/contact/updateContact')

const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");


const updateStatusContact = async (req, res) => {
  const { id } = req.params
  let { body } = req
  let { id: owner } = req.user
  
  if (req.user.status !== 'admin') {
    throw HttpError(404, `Access denied`)
  }
  
  let result = await updateContact({id, ownerid: req.user.id}, )
  
  if (!result) {
    throw HttpError(404, `Not found`)
  }
  res.json(result)
}

module.exports = {
  updateStatusContact: ctrlWrapper(updateStatusContact),
};
