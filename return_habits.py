import pymysql.cursors

# Returns all habits from specified UID

# Connect to the database
connection = pymysql.connect(host='test-db-instance.crtop2gwcupv.us-east-2.rds.amazonaws.com',
                             user='jonny_kidd',
                             password='mypassword',
                             )

cursor = connection.cursor()

sql = "use my_database"
cursor.execute(sql)

#Specify which uid
userid = 2

sql = ('''select * from habit where UID = (%i)''' % (userid))
cursor.execute(sql)
output = cursor.fetchall()

print(output)
