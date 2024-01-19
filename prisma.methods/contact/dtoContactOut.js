module.exports = function dtoContactOut(obPar) {
  let ob = obPar
  console.log('function dtoContactOut starts...')
  if ( ob.hasOwnProperty("nnumber") ) {
    ob.number = ob.nnumber
    delete ob.nnumber
  }
  
  if ( ob.hasOwnProperty("avatarurl") ) {
    ob.avatarUrl = ob.avatarurl
    delete ob.avatarurl
  }

  if ( ob.hasOwnProperty("id") ) {
    ob._id = String(ob.id)
    delete ob.id
  }

    if ( ob.hasOwnProperty("n") ) {
      ob.n = parseInt(ob.n)
  }

  if ( ob.hasOwnProperty("edrpu") ) {
    ob.edrpu = parseInt(ob.edrpu)
  }
  // console.log('function dtoContactOut return=', ob)
  return ob
}