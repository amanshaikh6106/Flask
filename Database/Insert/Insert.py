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
    sql = """INSERT INTO stud(student_id, name, age, course)values(%s, %s, %s, %s)"""
    values = (5, 'Aman', 20, 'Computer Science')
    cursor.execute(sql, values)
    con.commit()
   
except mysql.connector.Error as e:
    print("Error :", e)

finally:
    con.close() 
    cursor.close()
    
    print("Connection closed.")