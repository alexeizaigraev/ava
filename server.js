require('dotenv').config()

const app = require("./app");

const { DB_HOST, PORT } = process.env;


app.listen(PORT, () => {
  console.log(`Server running. Use our API on port: ${PORT}`);
});
