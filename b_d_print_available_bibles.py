from tinydb import TinyDB, Query
import b_a_parameters_bibles as pbs

db = TinyDB('b_c_db_bibles_'+pbs.LANGUAGE+'.json')

for bible in db:
    print(bible['id'] + '|' + bible['name'])


