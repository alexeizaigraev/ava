const updateUserPrisma = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const fs = require("fs/promises");
const { HttpError } = require("../../helpers");
const { cloudinary } = require("../../cloudinary");
const { ctrlWrapper } = require("../../decorators");

const updateUser = async (req, res) => {
  const { id } = req.user
  const { name, avatarurl } = req.body;
  if (!name && !avatarurl) {
    throw HttpError(
      404,
      "At least one field (name or avatarurl) must be provided."
    );
  }

  let cloudinaryavatarurl = req.user.avatarurl;

  if (req.file) {
    const { path: filePath, originalname } = req.file;

    const cloudinaryOptions = {
      folder: "avatars",
      allowed_formats: ["jpg", "jpeg", "png", "bmp"],
      publicid: `${originalname}_${id}`,
      transformation: { width: 100, height: 100, crop: "fill" },
      overwrite: true,
      secure: true,
    };

    const { secure_url } = await cloudinary.uploader.upload(
      filePath,
      cloudinaryOptions
    );

    cloudinaryavatarurl = secure_url;

    await fs.unlink(filePath);
  }

  const updateData = {};

  if (name) {
    updateData.name = name;
  }

  if (cloudinaryavatarurl) {
    updateData.avatarurl = cloudinaryavatarurl;
  }

  let newUser = await updateUserPrisma(  { id }, { name, cloudinaryavatarurl })
   
  res.status(201).json({
    avatarurl: newUser.avatarurl,
    name: newUser.name,
  });
};
module.exports = {
  updateUser: ctrlWrapper(updateUser),
};
