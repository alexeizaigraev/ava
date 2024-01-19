const {PrismaClient, prisma} = require('../../db')

module.exports = async function getUserById(idPar) {
  try {
    const user = await prisma.users.findUnique({
      where: {
        id: idPar
      }
    })
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
