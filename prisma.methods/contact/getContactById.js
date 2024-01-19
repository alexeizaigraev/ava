const {PrismaClient, prisma} = require('../../db')

module.exports = async function getContactById(idPar) {
  try {
    const user = await prisma.contacts.findUnique({
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
