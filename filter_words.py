import psycopg2
from dbconfig import dbname_, dbuser_, dbpassword_

#connect to the database
connection = psycopg2.connect("dbname='" + dbname_ + "' user='" + dbuser_ + "' password='" + dbpassword_ + "'")
connection.autocommit = True
cur = connection.cursor()

#take words to filter
filter_suffix = "%ъ"
sql = 'select * from public."chitanka_words" where word like %s'
cur.execute(sql, (filter_suffix,))
records = cur.fetchall()
words_to_filter = [row[1] for row in records]

#take all words from the database
sql = 'select * from public."chitanka_words"'
cur.execute(sql)
records = cur.fetchall()
all_words_list = [row[1] for row in records]

# #remove filtered words
# for word in words_to_filter:
#     if word[:len(word) - 1] in all_words_list:
#         sql = 'delete from public."chitanka_words"' + " where word = '" + word + "'"
#         cur.execute(sql)

for word in words_to_filter:
    sql = 'delete from public."chitanka_words"' + " where word = '" + word + "'"
    cur.execute(sql)

cur.close()
connection.close()