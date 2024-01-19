const {PrismaClient, prisma} = require('../../db')


module.exports = async function getContact(wherePar) {
  try {
    let contact = await prisma.contacts.findUnique({
      where: wherePar
    })
    // console.log(user)
    return contact
  } catch(e) {
    console.log(e)
  }
}
