import mysql.connector
from mysql.connector import Error 

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='learner_information',
                                         user='root',
                                         password='*y2u4*f,YEsJD(CF@<Ga')
    if connection.is_connected():
        server = connection.get_server_info()
        print("Connected to MySQL Server version ", server)

        cursor = connection.cursor()
        cursor.execute("select database();")
        db_name = cursor.fetchone()
        print("You're connected to database: ", db_name)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
