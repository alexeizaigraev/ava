CREATE TABLE audit 
(
 ID                 SERIAL          NOT NULL        PRIMARY KEY,
 Operation          VARCHAR         NOT NULL,
 DateTime           TimeStamp       NOT NULL,
 IDUser             TEXT            NOT NULL,
 QUERY              TEXT            NOT NULL,
 NameTable          TEXT            NOT NULL
);


CREATE OR REPLACE FUNCTION process_emp_audit() RETURNS TRIGGER AS $emp_audit$
    BEGIN

        IF (TG_OP = 'DELETE') THEN
            INSERT INTO audit (operation, datetime, iduser, query, nametable) SELECT 'Удалил', now(), user, current_query(),TG_TABLE_NAME;
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') THEN
            INSERT INTO audit (operation, datetime, iduser, query, nametable) SELECT 'Обновил', now(), user, current_query(),TG_TABLE_NAME;
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') THEN
            INSERT INTO audit (operation, datetime, iduser, query, nametable) SELECT 'Добавил', now(), user, current_query(),TG_TABLE_NAME;
            RETURN NEW;
        END IF;
        raise exception 'impossible TG_OP=%', TG_OP;
    END;
$emp_audit$ LANGUAGE plpgsql;


CREATE TRIGGER emp_audit1
AFTER INSERT OR UPDATE OR DELETE ON users
    FOR EACH ROW EXECUTE PROCEDURE process_emp_audit();

CREATE TRIGGER emp_audit2
AFTER INSERT OR UPDATE OR DELETE ON contacts
    FOR EACH ROW EXECUTE PROCEDURE process_emp_audit();