const createContact = require("./createContact")
const deleteContact = require("./deleteContact")
const dtoContactIn = require("./dtoContactIn")
const dtoContactOut = require("./dtoContactOut")
const getAllContacts = require("./getAllContacts")
const getContactById = require("./getContactById")
const updateContact = require("./updateContact")
const upsertContact = require("./upsertContact")


module.exports = {
  createContact,
  deleteContact,
  dtoContactIn,
  dtoContactOut,
  getAllContacts,
  getContactById,
  updateContact,
  upsertContact,
}
