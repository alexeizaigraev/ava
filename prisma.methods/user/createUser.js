const {PrismaClient, prisma} = require('../../db')


module.exports = async function createUser(dataPar) {
  try {
    const user = await prisma.users.create({
      data: dataPar,
    })
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
