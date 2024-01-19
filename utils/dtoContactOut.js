module.exports = function dtoContactOut(ob) {
  if ( ob.hasOwnProperty("nnumber") ) {
    ob.number = ob.nnumber
    delete ob.nnumber
  }
  return ob
}