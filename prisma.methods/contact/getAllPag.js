const {PrismaClient, prisma} = require('../../db')

module.exports = async function getAllPag(skip, take) {
  console.log("Starts getAllPag...")
  try {
    let data = await prisma.contacts.findMany({
      skip,
      take,
    })
    // console.log("data=", data)
    return data
  } catch(e) {
    console.log(e)
  }
}
