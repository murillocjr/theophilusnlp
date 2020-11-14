import c_a_parameters_bible as pb
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT token, count(*) as 'count' FROM wordtokens GROUP BY token ORDER by 2 desc; ''')

for row in cur:
	print(row)

conn.commit()
conn.close()
