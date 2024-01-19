const {PrismaClient, prisma} = require('../../db')


module.exports = async function updateContsct(wherePar, dataPar) {
  try {
    const contact = await prisma.contacts.update({
      where: wherePar,
      data: dataPar
    })
    // console.log(contact)
    return contact
  } catch(e) {
    console.log(e)
  }
}
