import sqlite3



class SqliteClient:

	def __init__(self,dbName):
		self.database = "sqlite"
		self.dbName = dbName
		self.createDatabase()
		self.createTable()

	def createDatabase(self):
		try:
		    sqliteConnection = sqlite3.connect(self.dbName)
		    cursor = sqliteConnection.cursor()
		    cursor.close()

		except sqlite3.Error as error:
		    print("Error while connecting to sqlite", error)
		finally:
		    if (sqliteConnection):
		        sqliteConnection.close()
		        print("The SQLite connection is closed")

	def createTable(self):
		try:
		    sqliteConnection = sqlite3.connect(self.dbName)
		    sqlite_create_table_query = '''CREATE TABLE flickr5 (
		                                image BLOB NOT NULL);'''

		    cursor = sqliteConnection.cursor()
		    print("Successfully Connected to SQLite")
		    cursor.execute(sqlite_create_table_query)
		    sqliteConnection.commit()
		    print("SQLite table created")
		    cursor.close()

		except sqlite3.Error as error:
		    print("Error while creating a sqlite table", error)
		finally:
		    if (sqliteConnection):
		        sqliteConnection.close()
		        print("sqlite connection is closed")


	def insertBLOB(self,imageBlob):
	    try:
	        sqliteConnection = sqlite3.connect(self.dbName)
	        cursor = sqliteConnection.cursor()
	        print("Connected to SQLite")
	        sqlite_insert_blob_query = """INSERT INTO flickr5
	                                  (image) VALUES (?)"""

	        data_tuple = (imageBlob,)
	        cursor.execute(sqlite_insert_blob_query, data_tuple)
	        sqliteConnection.commit()
	        cursor.close()

	    except sqlite3.Error as error:
	        print("Failed to insert blob data into sqlite table", error)
	    finally:
	        if (sqliteConnection):
	            sqliteConnection.close()
	            print("the sqlite connection is closed")








