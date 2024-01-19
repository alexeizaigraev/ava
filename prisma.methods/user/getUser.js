const {PrismaClient, prisma} = require('../../db')


module.exports = async function getUser(wherePar) {
  try {
    const user = await prisma.users.findUnique({
      where: wherePar
    })
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
