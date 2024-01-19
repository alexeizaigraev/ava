const updateContactPrisma = require('../../prisma.methods/contact/updateContact')
const dtoContactIn = require('../../prisma.methods/contact/dtoContactIn')

const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");

const updateContact = async (req, res) => {
  console.log('updateContact starts...')
  let idPar = parseInt( req.params.id)
  console.log("req.params.id", req.params.id)
  let body = req.body
  // body = dtoContactIn(body)
    
  const idUser = req.user.id;
  
  let result = await updateContactPrisma({id: idPar}, dtoContactIn(body))
  
  if (!result) {
    throw HttpError(404, `Not found`);
  }
  
  res.json(result);
};

module.exports = {
  updateContact: ctrlWrapper(updateContact),
};
