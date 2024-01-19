const getAllPag = require('../../prisma.methods/contact/getAllPag')
const getContact = require('../../prisma.methods/contact/getContact')
const dtoContactOutMany = require('../../prisma.methods/contact/dtoContactOutMany')
const dtoContactOut = require('../../prisma.methods/contact/dtoContactOut')

const { ctrlWrapper } = require("../../decorators");

const getAllContacts = async (req, res) => {
  // console.log('start getAllContacts...')
  // console.log('req=', req)
  const { id: ownerid, status: status, email } = req.user;
  // console.log('req.user=', req.user)
  
  // const { page = 1, limit = 20, favorite } = req.query;
  // const { page0, limit = 2 } = req.query;

  const limit = 20
  let page = req.body.page
  // console.log("req.body=", req.body)
  // console.log('page=', page, typeof page)
  
  page=1
  const skip = (page - 1) * limit;


  let result;

  if (status === 'admin') {
  result = await getAllPag(skip, limit)
  // console.log("result=", result)
  res.json(dtoContactOutMany(result))
  } else {
    result = await getContact( {email} )
    res.json([dtoContactOut(result)])
  }
};

module.exports = {
  getAllContacts: ctrlWrapper(getAllContacts),
};
