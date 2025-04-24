import sqlite3

rankDatabaseConnection = sqlite3.connect('../data/excuses_ranks.db')
cursor = rankDatabaseConnection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Excuses (
id INTEGER,
text TEXT,
rank INTEGER
)
''')

cursor.execute('INSERT INTO Excuses (id, text, rank) VALUES (?, ?, ?)', (1, "My cat eat my frige!", 14))

rankDatabaseConnection.commit()
rankDatabaseConnection.close()