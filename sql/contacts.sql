DROP TABLE IF EXISTS contacts  CASCADE;

CREATE TABLE contacts (
  id SERIAL PRIMARY KEY,
  n TEXT,
  form TEXT,
  nnumber TEXT,
  fio TEXT,
  edrpu TEXT,
  passport TEXT,
  birthday TEXT,
  registrationplase TEXT,
  adress TEXT,
  phone TEXT,
  email TEXT NOT NULL UNIQUE,
  membershipfee NUMERIC(20,2),
  share NUMERIC(20,2),
  payshare NUMERIC(20,2),
  avatarurl TEXT,
  ownerid INTEGER NOT NULL,

  CONSTRAINT contacts_fkey_ownerid FOREIGN KEY (ownerid) REFERENCES users (id)
  ON DELETE CASCADE
);
