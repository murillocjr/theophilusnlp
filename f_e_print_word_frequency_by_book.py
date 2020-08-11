import c_a_parameters_bible as pb
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT book,token, count(*) as 'count' FROM wordtokens GROUP BY book,token ORDER by 1,3 desc; ''')

old_book = ""
token_count = 0
line = ""
for row in cur:
	book = row[0]
	token = row[1]
	count = row[2]

	if(old_book != book):
		token_count = 0
		old_book = book
		print(line)
		line = book + "\t"
	else:
		token_count += 1
		if(token_count<4):
			line = line + token + "(" + str(count) + ")"  + "\t\t"
conn.commit()
conn.close()
