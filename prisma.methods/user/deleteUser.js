const {PrismaClient, prisma} = require('../../db')


module.exports = async function deleteUser(wherePar) {
  try {
    const user = await prisma.users.delete({
      where: wherePar
    })
    // console.log(user)
    return user
  } catch(e) {
    console.log(e)
  }
}
