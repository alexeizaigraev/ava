const deleteContactPrisma = require('../../prisma.methods/contact/deleteContact')
const dtoContactIn = require('../../prisma.methods/contact/dtoContactIn')

const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");

const removeContact = async (req, res) => {
  console.log('req.params=', req.params)
  const id = parseInt(req.params.id)
  const { body } = req;
  const idUser = req.user.id;
  let result = await deleteContactPrisma({ id }, body);
  
  if (!result) {
    throw HttpError(404, `Not found`);
  }
  res.json(result)
};

module.exports = {
  removeContact: ctrlWrapper(removeContact),
};
