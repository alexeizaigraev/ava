const dtoContactOut = require('./dtoContactOut')

module.exports = function dtoContactOutMany(arr) {
  console.log('function dtoContactOutMany starts...')
  for (let i = 0; i < arr.length; i++) {
    console.log(i)
    let ob = dtoContactOut(arr[i])
    arr[i] = ob
  }
  // console.log("arr=", arr)
  return arr
}