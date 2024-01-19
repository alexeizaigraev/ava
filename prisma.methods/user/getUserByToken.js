const {PrismaClient, prisma} = require('../../db')

module.exports = async function getUserByToken(wherePar) {
  try {
    const user = await prisma.users.findUnique({
      where: wherePar
    })
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
