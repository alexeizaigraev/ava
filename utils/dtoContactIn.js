module.exports = function dtoContactIn(ob) {
  if ( ob.hasOwnProperty("number") ) {
    ob.nnumber = ob.number
    delete ob.number
  }
  return ob
}
