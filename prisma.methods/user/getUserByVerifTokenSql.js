const {PrismaClient, prisma} = require('../../db')

module.exports = async function getUserByVerifTokenSql(verifTokenPar) {
  try {
    const user = await prisma.$queryRaw`SELECT * FROM users 
    WHERE verificationtoken = ${verifTokenPar}`
    if (user.length === 1) {
      // console.log(user[0])
      return user[0]
    }
  } catch(e) {
    console.log(e)
  }
}
