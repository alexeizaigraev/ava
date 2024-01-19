const {PrismaClient, prisma} = require('../../db')

module.exports = async function getUserByPassword(passPar) {
  try {
    const user = await prisma.$queryRaw`SELECT * FROM users WHERE
    password = ${passPar}`
    if (user.length === 1) {
      // console.log('user: ', user[0])
      return user[0]
    }
  } catch(e) {
    console.log(e)
  }
}
