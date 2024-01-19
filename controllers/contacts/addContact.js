const createContact = require('../../prisma.methods/contact/createContact')

const dtoContactIn = require('../../prisma.methods/contact/dtoContactIn')
const { ctrlWrapper } = require("../../decorators")


const addContact = async (req, res) => {
  console.log('addContact starts...')
  console.log("req.user=", req.user)
  let body = req.body
  // console.log('body=', body)
  // let bodyDtoIn = dtoContactIn(body)
  // console.log("req.user=", req.user)
  const idUser = req.user.id;
  console.log("idUser", idUser)
  body.ownerid = idUser
  // console.log("body=", body)
  
  let result = createContact(dtoContactIn(body))
  res.json(result)
}

module.exports = {
  addContact: ctrlWrapper(addContact),
}
