import psycopg2
import csv
from dbconfig import dbname_, dbuser_, dbpassword_

def createTables():    
    command = ('''

    CREATE TABLE IF NOT EXISTS "chitanka_words" (
        "id" varchar PRIMARY KEY,
        "word" varchar UNIQUE
    );
    
    ''')

    #connect to the database
    connection = psycopg2.connect("dbname='" + dbname_ + "' user='" + dbuser_ + "' password='" + dbpassword_ + "'")
    connection.autocommit = True
    cur = connection.cursor()

    connection = None
    try:
        #create the tables in the database
        cur.execute(command)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def importData():
    try:
        #connect to the database
        connection = psycopg2.connect("dbname='" + dbname_ + "' user='" + dbuser_ + "' password='" + dbpassword_ + "'")
        connection.autocommit = True
        cur = connection.cursor()

        f = open("../unique_words_3.txt", encoding="utf-8", mode="r")
        file_contents = f.read().split("\n")
        f.close()

        word_id = 1
        sql = 'insert into public."chitanka_words" (id, word) values(%s, %s);'
        for word in file_contents:
            try:
                cur.execute(sql, (str(word_id), word))
                word_id+=1
            except:
                print("skipping word: " + word)
                word_id+=1
            
        f.close()
        
        connection.commit()
    except psycopg2.Error as e:
        print(e)
    
    cur.close()
    connection.close()

if __name__ == '__main__':
    createTables()
    importData()