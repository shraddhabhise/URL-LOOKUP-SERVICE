import sqlite3


conn = sqlite3.connect('/Users/shraddhabhise/PycharmProjects/URL-LOOKUP-SERVICE/api/database.db')
print("Opened database successfully");

#conn.execute('CREATE TABLE malwareurls (url TEXT)')
#print( "Table malwareurls created successfully");
conn.execute('CREATE TABLE malwarehosts (url TEXT)')
print( "Table malwarehosts created successfully");
conn.close()