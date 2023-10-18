import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1873"
  )

# Prepare a cursor object
mycursor = db.cursor()

# Create the database
mycursor.execute("CREATE DATABASE dcrm_db")