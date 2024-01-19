const updateUser = require('../prisma.methods/user/updateUser')
const getUser = require('../prisma.methods/user/getUser')

const jwt = require("jsonwebtoken");

const { HttpError } = require("../helpers");

const { SECRET_KEY } = process.env;

const authenticate = async (req, res, next) => {
  const { authorization = "" } = req.headers;
  
  const [bearer, token] = authorization.split(" ");
  if (bearer !== "Bearer" || !token) {
    next(HttpError(401, "Not authorized *"));
  }
  try {
    const { id } = jwt.verify(token, SECRET_KEY);

    const decoded = jwt.verify(token, SECRET_KEY)
    const user = await getUser( {id} )

    if (!user || !user.token || user.token !== token) {
      console.log("# user not found!")
      next(HttpError(401, "Not authorized"));
    }
    req.user = user;
    next();
  } catch {
    next(HttpError(401, "Not authorized"));
  }
};

module.exports = authenticate;
