import mysql.connector
try:
    con = mysql.connector.connect(
        host="localhost",
        user="Aman",
        password="Aman@6106",
        database="my_database"
    )
    if con.is_connected():
        print("connected sucessfully")
    cursor = con.cursor()
    sql = """UPDATE stud SET name = %s, age = %s, course = %s WHERE student_id = %s"""
    values = ('Aman', 21, 'Data Science', 5)
    cursor.execute(sql, values)
    con.commit()
    print(cursor.rowcount, "row(s) updated.")

except mysql.connector.Error as e:
    print("Error :", e)

finally:
    con.close() 
    cursor.close()
    print("Connection closed.")