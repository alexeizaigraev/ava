const {PrismaClient, prisma} = require('../../db')


module.exports = async function upsertUser(dataPar) {
  console.log('upsertUser, dataPar=', dataPar)
  try {
    const user = await prisma.users.upsert({
      where: {
        email: dataPar.email,
      },
      create: dataPar,
      update: dataPar,
      select: {id: true, email: true, name: true}
    })
    console.log('upsertUser=', user)
    return user
  } catch(e) {
    console.log(e)
  }
}
