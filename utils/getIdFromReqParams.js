module.exports = function getIdFromReqParams(requestParams) {
  let idPar = ''
  try {
    idPar = requestParams.id
  } catch(e) {
    // console.log(e)
  }

  if ( !idPar ) {
    try {
      idPar = req.params._id
    } catch(e) {
      // console.log(e)
    }  
  }
  return idPar
}