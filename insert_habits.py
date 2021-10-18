import pymysql
import pyodbc
import pandas as pd

# Creates a new table of habits from habits.csv

# Reads habits into DataFrame
df = pd.read_csv("habits.csv")

#Connecting to DB Server
connection = pymysql.connect(host='test-db-instance.crtop2gwcupv.us-east-2.rds.amazonaws.com',
                             user='jonny_kidd',
                             password='mypassword',
                             )

cursor = connection.cursor()

# Creating new DB
sql = "drop database my_database"
cursor.execute(sql)
cursor.connection.commit()

sql = "create database my_database"
cursor.execute(sql)
cursor.connection.commit()

sql = "use my_database"
cursor.execute(sql)

# Creating new Table
sql = '''
create table habit (
id int not null auto_increment,
uid int,
username text,
habit_name text,
habit_frequency text,
deterioration_value int,
primary key (id)
)
'''
cursor.execute(sql)

# Insert each habit from Dataframe into SQL Server:
for index, row in df.iterrows():
        sql = '''
        insert into habit(uid,username,habit_name,habit_frequency,deterioration_value) values('%i','%s','%s','%s','%i')''' % (row.UID,row.User_Name,row.Habit_Name,row.Habit_Frequency,row.Deterioration_Value)
        cursor.execute(sql)

connection.commit()
cursor.close()
