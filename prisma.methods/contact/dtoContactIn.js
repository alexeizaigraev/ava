module.exports = function dtoContactIn(obPar) {
  let ob = obPar
  console.log('function dtoContactIn starts...')
  if ( ob.hasOwnProperty("number") ) {
    ob.nnumber = ob.number
    delete ob.number
  }
  
  if ( ob.hasOwnProperty("avatarUrl") ) {
    ob.avatarurl = ob.avatarUrl
    delete ob.avatarUrl
  }

  if ( ob.hasOwnProperty("_id") ) {
    ob.id = parseInt(ob._id)
    delete ob._id
  }

    if ( ob.hasOwnProperty("n") ) {
      ob.n = String(ob.n)
  }

  if ( ob.hasOwnProperty("edrpu") ) {
    ob.edrpu = String(ob.edrpu)
    console.log(ob.edrpu, typeof ob.edrpu)
  }
  console.log('function dtoContactIn return=', ob)
  return ob
}