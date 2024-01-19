const {PrismaClient, prisma} = require('../../db')

module.exports = async function isUserExistsByEmail(emailPar) {
  try {
    let result = await prisma.$queryRaw`SELECT count(*) FROM users WHERE email = ${emailPar}`
    result = result[0].count
    console.log('result= ', result)
    if (result > 0) {
      console.log(true)
      return true
    } else {
      console.log(false)
      return false
    }
  } catch(e) {
    console.log(e)
  }
}
