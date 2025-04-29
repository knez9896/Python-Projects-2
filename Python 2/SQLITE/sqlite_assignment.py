Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> with sqlite3.connect('test_database.db') as connection:
...         c = connection.cursor()
...         c.executescript("""DROP TABLE IF EXISTS People;
...                         CREATE TABLE People (FirstName TEXT, LastName TESXT, Age INT);
...                         INSERT INTO People VALUES ('Ron', 'Obvious', '42');
...                         """)
... 
<sqlite3.Cursor object at 0x0000025679A18540>
>>> peopleValues = (('Luigi', 'Vercotti', 43), ('Artuhur', 'Belling', 28))
>>> c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
<sqlite3.Cursor object at 0x0000025679A18540>
