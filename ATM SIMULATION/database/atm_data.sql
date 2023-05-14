import sqlite3

# Connect to the database
conn = sqlite3.connect('atm.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name VARCHAR(255), face VARCHAR(255), fingerprint VARCHAR(255), balance INTEGER, email VARCHAR(255), date_of_birth DATE, gender VARCHAR(255), country_of_residence VARCHAR(255), mobile_number VARCHAR(255))')

# Insert some data
c.execute('INSERT INTO users (name, face, fingerprint, balance, email, date_of_birth, gender, country_of_residence, mobile_number) VALUES ("John Doe", "face.png", "fingerprint.png", 1000, "johndoe@example.com", "1990-01-01", "male", "United States", "123-456-7890")')
c.execute('INSERT INTO users (name, face, fingerprint, balance, email, date_of_birth, gender, country_of_residence, mobile_number) VALUES ("Jane Doe", "face.png", "fingerprint.png", 2000, "janedoe@example.com", "1991-02-02", "female", "Canada", "987-654-3210")')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
