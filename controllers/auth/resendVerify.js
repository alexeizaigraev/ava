const updateUser = require('../../prisma.methods/user/updateUser')
const getUser = require('../../prisma.methods/user/getUser')

const { ctrlWrapper } = require("../../decorators");
const { HttpError } = require("../../helpers");
const { BASE_URL } = process.env;


const resendVerify = async (req, res) => {
  const { email } = req.body;

  let user = await getUser( {email} )
  
  if (!user) {
    throw HttpError(404, "User not found");
  }
  if (user.verify) {
    throw HttpError(400, "Verification has already been passed");
  }
  const link = `${BASE_URL}/api/auth/verify/${user.verificationToken}`
  console.log('resend link=', link)
  const verifyEmail = {
    to: email,
    subject: "Сonfirm your registration",
    html: `<a target="_blank" href="${BASE_URL}/api/auth/verify/${user.verificationToken}">Click to confirm your registration</a>`,
  };

  await sendEmail(verifyEmail);

  res.json({
    message: "Verification email sent",
  });
};
module.exports = {
  resendVerify: ctrlWrapper(resendVerify),
};
