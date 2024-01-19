const {PrismaClient, prisma} = require('../../db')


module.exports = async function deleteContact(wherePar) {
  try {
    const contact = await prisma.contacts.delete({
      where: wherePar
    })
    // console.log(contact)
    return contact
  } catch(e) {
    console.log(e)
  }
}
