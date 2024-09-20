import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd = "clockmate",
    database = "python_database"
    
)

cursor = db.cursor()

table_name = input("Enter table name : ")


select = f"select * from {table_name}"
try:
    cursor.execute(select)
    result = cursor.fetchall()


    for row in result:
        length = len(row)
        for num in range(0, length):
            print(f"{row[num]}")
        print(" ")
     

except:
    print(f"the table named {table_name} not found ")






 