import sqlite3

# db = sqlite3.connect('server.db')
# sql = db.cursor()

# sql.execute("""CREATE TABLE IF NOT EXISTS users(
#     loing TEXT,
#     password TEXT,
#     email VARCHAR(25)
# )
# """)


# Check
def show_all():
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute("SELECT rowid, * FROM users")
    items = sql.fetchall()

    for item in items:
        print(item)
    

    db.commit()
    print('Commit')

    db.close() 

# Add one
def add_one(first,last,email):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute("INSERT INTO users VALUES (?,?,?)", (first,last,email))
    db.commit()
    db.close()

# Add many
def add_many(list):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.executemany("INSERT INTO users VALUES (?,?,?)", (list))

    db.commit()
    db.close()

# Search by email
def email_search(email):
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute("SELECT * FROM users WHERE email = (?)", (email,))


    items = sql.fetchall()

    for item in items:
        print(item)

    db.commit()
    db.close()

# Delete user
def delete_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute("DELETE FROM users WHERE rowid = (?)", id)

    db.commit()
    db.close()

