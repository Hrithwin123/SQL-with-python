import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "clockmate",
    database = "python_database"

)

cursor = db.cursor()

insert ="insert into employees(name, salary) values(%s, %s);"
rows = []
row = ()
n = int(input("Enter the number of rows : "))

for i in range(1, n+1):
    name = input(f"Enter the name of employee {i} : ")
    salary = int(input(f"Enter the salary of {name} : "))
    row = (name, salary)
    rows.append(row)


for i in rows:
    cursor.execute(insert, i)

db.commit()

print("program ran succesfully!!")

