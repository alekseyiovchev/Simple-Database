import sqlitetest


sqlitetest.add_one('John','Pary','pery@gmail.com')

sqlitetest.delete_user('3')

people = [
    ('Tim', 'Mackson', 'tim@yahoo.com'),
    ('Miy', 'Clen', 'clen@gmail.com'),
    ('Sick', 'Brick','brick@gmail.com')
    ]

sqlitetest.add_many(people)

sqlitetest.email_search('tim@yahoo.com')

sqlitetest.show_all()