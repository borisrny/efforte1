from psycopg2 import extras
from src.util import pg_get_connection, pg_return_connection


def facility_base_list(cnf, f_type, fltr):
    con = pg_get_connection(cnf['pg'])
    cur = con.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('SELECT * FROM facility WHERE facilitytype=%s', (f_type,))
    data = [i for i in cur.fetchall()]
    cur.close()
    pg_return_connection(con)
    return data
