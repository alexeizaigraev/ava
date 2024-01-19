const {PrismaClient, prisma} = require('../../db')

module.exports = async function getAllUContacts() {
  try {
    const user = await prisma.contacts.findMany()
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
