import psycopg2
from dbconfig import dbname_, dbuser_, dbpassword_

#connect to the database
connection = psycopg2.connect("dbname='" + dbname_ + "' user='" + dbuser_ + "' password='" + dbpassword_ + "'")
connection.autocommit = True
cur = connection.cursor()

#get filtered words
filter_suffix = "%ме"
sql = 'select * from public."chitanka_words" where word like %s'
cur.execute(sql, (filter_suffix,))
records = cur.fetchall()
words_to_filter = [row[1] for row in records]

#get all words in the database
sql = 'select * from public."chitanka_words"'
cur.execute(sql)
records = cur.fetchall()
all_words_list = [row[1] for row in records]

#remove filtered words
for word in words_to_filter:
    print(word)
    if word[:len(word) - 1] in all_words_list:
        print(word[:len(word) - 1])
        sql = 'delete from public."chitanka_words"' + " where word = '" + word + "'"
        print(sql)
        cur.execute(sql)

cur.close()
connection.close()