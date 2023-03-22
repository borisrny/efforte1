SQL="
CREATE DATABASE pci
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
"
#PGPASSWORD=${PASSWD}  psql -h ${HOST} -U ${USER} -d ${DB} -c "${SQL}"






TABLE='notification'
SQL="
drop TABLE IF EXISTS ${SCHEMA}.${TABLE};
create TABLE ${SCHEMA}.${TABLE}
(
  id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
  text character varying,
  cratedate TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"
PGPASSWORD=${PASSWD}  psql -h ${HOST} -U ${USER} -d ${DB} -c "${SQL}"


