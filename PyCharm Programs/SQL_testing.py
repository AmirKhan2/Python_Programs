import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-VSBE2G9;'
                      'Database=AdventureWorks2017;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


cursor.execute('SELECT * FROM AdventureWorks2017.Person.BusinessEntityContact')

for row in cursor:
    print(row)
