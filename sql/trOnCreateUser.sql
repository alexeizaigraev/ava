CREATE OR REPLACE FUNCTION insertusertocontactsfunc() RETURNS TRIGGER AS $my_table$
   BEGIN
      INSERT INTO contacts(fio, email, avatarurl, ownerid 
      ) VALUES (
        new.name, new.email, new.avatarurl, new.id);
      RETURN NEW;
   END;
$my_table$ LANGUAGE plpgsql;


CREATE TRIGGER insertusertocontacts_trigger AFTER INSERT ON users
FOR EACH ROW EXECUTE PROCEDURE insertusertocontactsfunc();