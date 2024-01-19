const {PrismaClient, prisma} = require('../../db')


module.exports = async function updateUser(wherePar, dataPar) {
  try {
    const user = await prisma.users.update({
      where: wherePar,
      data: dataPar
    })
    console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
