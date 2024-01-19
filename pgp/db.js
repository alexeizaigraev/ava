const monitor = require('pg-monitor')

const connectionString = require('../db.config')
var promise = require('bluebird');

var options = {
  query(e) {
    console.log('QUERY:', e.query);
},
  // Initialization Options
  promiseLib: promise
};

var pgp = require('pg-promise')(options);
monitor.attach(options, ['query', 'error'])

var db = pgp(connectionString);

// add query functions

module.exports = db
