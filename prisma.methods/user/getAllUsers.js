const {PrismaClient, prisma} = require('../../db')

module.exports = async function getAllUsers() {
  try {
    const user = await prisma.users.findMany()
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
