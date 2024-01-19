const {PrismaClient, prisma} = require('../../db')

module.exports = async function getUserByEmailPassword(emailPar, passPar) {
  try {
    const user = await prisma.$queryRaw`SELECT * FROM users WHERE email = ${emailPar}
    AND password = ${passPar}`
    if (user.length === 1) {
      // console.log(user[0])
      return user[0]
    }
  } catch(e) {
    console.log(e)
  }
}
