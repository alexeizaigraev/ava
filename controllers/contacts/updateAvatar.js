const updateContact = require('../../prisma.methods/contact/updateContact')

const fs = require("fs/promises");
const Jimp = require("jimp");
const path = require("path");

// const { User } = require("../../models/user");
const { Contact } = require("../../models/contacts");
const { HttpError } = require("../../helpers");
const { ctrlWrapper } = require("../../decorators");

const avatarDir = path.resolve("public", "avatars");

const updateAvatar = async (req, res, next) => {
  // Check if avatar file was provided in the request
  if (!req.file) {
    throw HttpError(400, "Avatar must be provided");
  }

  const { id } = req.user;
  const { path: tempUpload, originalname } = req.file;

  // Resize and save the avatar using Jimp library
  await Jimp.read(tempUpload)
    .then((avatar) => {
      return avatar
        .resize(250, 250) // resize to 250x250 pixels
        .quality(100) // set JPEG quality to 100
        .write(tempUpload); // save the changes
    })
    .catch((err) => {
      throw err;
    });

  const fileName = `${id}_${originalname}`;

  const publicUpload = path.join(avatarDir, fileName);

  // Move the uploaded file from temp directory to public avatars directory
  await fs.rename(tempUpload, publicUpload);

  const avatarurl = path.join("avatars", fileName);

  // Update the user's avatarurl field in the database
   let result = await updateContact({id}, {avatarurl})

  result = result.avatarurl
    // Respond with the updated avatar URL
  res.json({
    result
  });
};

// Export the controller with ctrlWrapper decorator applied
module.exports = {
  updateAvatar: ctrlWrapper(updateAvatar),
};
