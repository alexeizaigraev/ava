const {PrismaClient, prisma} = require('../../db')


module.exports = async function createContact(dataPar) {
  console.log('createContact, dataPar=', dataPar)
  // let dataInsert = {
  //   n: dataPar.n || '',
  //   form: dataPar.form || '',
  //   nnumber: dataPar.nnumber || '',
  //   fio: dataPar.fio || '',
  //   edrpu: dataPar.edrpu || '',
  //   passport: dataPar.passport || '',
  //   birthday: dataPar.birthday || '',
  //   registrationplase: dataPar.registrationplase || '',
  //   adress: dataPar.adress || '',
  //   phone: dataPar.phone || '',
  //   email: dataPar.email,
  //   membershipfee: dataPar.membershipfee || 0.00,
  //   share: dataPar.share || 0.00,
  //   payshare: dataPar.payshare || 0.00,
  //   avatarurl: dataPar.avatarurl || '',
  //   ownerid: dataPar.ownerid
  // }
  // console.log(dataInsert)
  try {
    let contact = await prisma.contacts.create({
      data: dataPar,
    })
    // console.log(contact)
    return contact
  } catch(e) {
    console.log(e)
  }
}
