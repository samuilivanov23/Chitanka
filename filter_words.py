import psycopg2
from dbconfig import dbname_, dbuser_, dbpassword_

#connect to the database
connection = psycopg2.connect("dbname='" + dbname_ + "' user='" + dbuser_ + "' password='" + dbpassword_ + "'")
connection.autocommit = True
cur = connection.cursor()

#get filtered words
filter_suffix = "%ят"
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
    all_words_list.remove(word)

#delete rows from table 'chitanka_words'
sql = 'delete from public."chitanka_words"'
cur.execute(sql)
connection.commit()

#populate the table 'chitanka_words' with the filtered list
word_id = 1
sql = 'insert into public."chitanka_words" (id, word) values(%s, %s);'
for word in all_words_list:
    try:
        cur.execute(sql, (str(word_id), word))
        word_id+=1
    except:
        print("skipping word: " + word)
        word_id+=1
    
connection.commit()

cur.close()
connection.close()