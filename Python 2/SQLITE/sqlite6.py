import sqlite3

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

with sqlite3.connect('test_database.db') as connection:
    c = conneciton.cursor()
    c.execute("INSTER INTO PEOPLE VALUES(?, ?, ?)", personData)

c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))
