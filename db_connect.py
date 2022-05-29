import mysql.connector as mysql

db = mysql.connect(
    host='localhost',
    user='root',
    passwd='Emmyboy1705#',
    database='testdatabase'
) 

mycursor = db.cursor()

mycursor.execute('DROP TABLE Person')

mycursor.execute('CREATE TABLE Person (name VARCHAR(50), age int UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)')

mycursor.execute('DESCRIBE Person')

mycursor.execute('INSERT INTO Person (name, age) VALUES ("Emma", 21)')

db.commit()

mycursor.execute('SELECT * FROM Person')

for x in mycursor:
    print(x)

a = 54

assert a == 56, "a should be equal to 56"

