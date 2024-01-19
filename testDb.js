const {db} = require('./db')

async function f() {
  const r = await db.users.findByEmail('123')
  console.log(r)
}

f()