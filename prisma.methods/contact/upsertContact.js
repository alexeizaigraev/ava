const {PrismaClient, prisma} = require('../../db')


module.exports = async function upsertContact(dataPar) {
  console.log('upsertContact, dataPar=', dataPar)
  try {
    const contact = await prisma.contacts.upsert({
      where: {
        email: dataPar.email,
      },
      create: dataPar,
      update: dataPar,
      select: {id: true, email: true, name: true}
    })
    console.log('upsertContact=', contact)
    return contact
  } catch(e) {
    console.log(e)
  }
}
