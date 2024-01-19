DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  subscription TEXT,
  status TEXT,
  token TEXT,
  avatarurl TEXT,
  verify BOOLEAN,
  verificationtoken TEXT
);
