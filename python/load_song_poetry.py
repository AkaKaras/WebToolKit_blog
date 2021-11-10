# -*- coding: UTF-8 -*-
import json
import mysql.connector #the module name is mysql-connector-python
import glob
import timeit


#open files and store the files in a list
song_poet_files = glob.glob("C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/poet.song.*.json")

#song_authors file path
song_authors_file = "C:/Users/chun_/Documents/programing_learning/chinese-poetry/json/authors.song.json"


#connect to local database
#make sure the database character and collection are set utf8mb4/utf8mb4_0900_ai_ci
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Mysql956028374l",
	database="chinese_poetry")

mycursor = mydb.cursor(buffered=True)

#drop table if exists
mycursor.execute("SET FOREIGN_KEY_CHECKS=0")
mycursor.execute("SET NAMES utf8mb4")
mycursor.execute("drop table if exists chinese_poetry.song_authors")
mycursor.execute("drop table if exists chinese_poetry.song_poets")
mycursor.execute("drop table if exists chinese_poetry.song_paragraphs")

#create table
mycursor.execute("""create table chinese_poetry.song_authors (
                    `id` int not null auto_increment,
                    `name` varchar(50) null,
                    `desc` text null,
                    primary key (`id`))
                    CHARACTER SET utf8mb4,COLLATE = utf8mb4_0900_ai_ci""")

mycursor.execute("""create table chinese_poetry.song_poets (
                    `id` int not null,
                    `title` text null,
                    `author_id` int null,
                    primary key (`id`),
                    foreign key (`author_id`) references song_authors(`id`))
                    CHARACTER SET utf8mb4,COLLATE = utf8mb4_0900_ai_ci""")

mycursor.execute("""create table chinese_poetry.song_paragraphs (
                    `id` int not null,
                    `poet_id` int not null,
                    `index` int not null,
                    `sentence` text null,
                    primary key (`id`),
                    foreign key (`poet_id`) references song_poets(`id`))
                    CHARACTER SET utf8mb4,COLLATE = utf8mb4_0900_ai_ci""")

with open(song_authors_file, 'r', encoding='utf-8') as j:
    data = json.loads(j.read())

author_list = []

for d in data:
    author_list.append((d['name'],d['desc']))


sql = "insert into song_authors(`name`, `desc`) values (%s, %s)"
mycursor.executemany(sql,author_list)

print("authors file is loaded")
    
#for insert id
poet_id = 0
sentence_id = 0
author_id = 0



#loop each json file
for file in song_poet_files:
    
    start = timeit.default_timer()
    print(file)

    #open the file
    with open(file,'r',encoding="utf-8") as j:
        #load the file into json format
        data = json.loads(j.read())

    poet_list = []
    paragraph_list = []
    author_name = ""
    #read each data
    for poet in data:
        poet_id += 1
        author = poet['author']

        if author_name != author:
            author_name = author
            #retrieve the author's id in song_authors table
            sql = "select `id` from chinese_poetry.song_authors where name like %s COLLATE utf8mb4_general_ci"
            mycursor.execute(sql,(author,))
            author_id = mycursor.fetchone()[0]
    
        title = poet['title']
        #insert data to song_poets table
        poet_list.append((poet_id,author_id,title))

        paragraphs = poet['paragraphs']

        #insert data to song_paragraphs table
        for ind in range(len(paragraphs)):
            sentence_id += 1
            sentence = paragraphs[ind]
            paragraph_list.append((sentence_id,poet_id, ind, sentence))

    
    sql = "insert into song_poets(id, author_id, title) values (%s, %s, %s)"
    mycursor.executemany(sql,poet_list)#<---speed up the insert speed!!!!

    sql = "insert into song_paragraphs(id, poet_id, `index`, sentence) values (%s, %s, %s, %s)"

    mycursor.executemany(sql,paragraph_list)
    
    print(file,"done")
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    # close file
    j.close() 
    

#close cursor
mydb.commit()
mycursor.close()
mydb.close()
print("loaded")


