const db = require('../../pgp/db')
const dtoContactOut = require('../../utils/dtoContactOut.js')

const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");

const getContactById = async (req, res) => {
  console.log('req.params=', req.params)
  let  _id = req.params.id
  console.log('_id=', _id, typeof _id)
  db.any(`SELECT * FROM contacts
  WHERE _id = $1`, [ _id ])
  .then(function(data) {
    if (data) {
      console.log('data=', data)
      res.json(dtoContactOut(data))
    }
    else {
      throw HttpError(404, `Not found`)
    }
  })
};

module.exports = {
  getContactById: ctrlWrapper(getContactById),
};
