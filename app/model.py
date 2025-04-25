import sqlite3
from sqlite3 import Cursor
import os

#Create DB if not exist
def create_excuses_db():
    #Create folder for DB if not exist
    try:
        os.mkdir("../data")
    except FileExistsError:
        ...
    #Connect to DB
    rankDatabaseConnection = sqlite3.connect('../data/excuses_ranks.db')
    cursor = rankDatabaseConnection.cursor()
    #Create DB if not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Excuses (
    id INTEGER,
    text TEXT,
    rank INTEGER
    )
    ''')
    rankDatabaseConnection.commit()
    cursor.close()
    rankDatabaseConnection.close()

#Check if element exist in DB by 'text'
def check_if_exist(text: str, cursor: Cursor):
    cursor.execute('SELECT * FROM Excuses WHERE text = ? LIMIT 1', (text,))
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False

#Add excuse to BD
def add_excuse(text: str, cursor: Cursor):
    #Check if element not already exsist
    if (not check_if_exist(text, cursor)):
        #Find max id
        result_max_id = cursor.execute('SELECT MAX(id) FROM Excuses').fetchone()
        if(result_max_id[0] is not None):
            max_id = result_max_id[0]
        else:
            max_id = 0
        #Insert new element
        cursor.execute('INSERT INTO Excuses (id, text, rank) VALUES (?, ?, ?)', (max_id + 1, text, 0))
       

#Change 'rank' in BD and delete element if 'rank' < 1
def change_rank(text: str, deltaRank: int):
    #Connect to DB
    rankDatabaseConnection = sqlite3.connect('../data/excuses_ranks.db')
    cursor = rankDatabaseConnection.cursor()
    #Try to add element
    add_excuse(text, cursor)
    #Update'rank'
    cursor.execute('UPDATE Excuses SET rank = rank + ? WHERE text = ?', (deltaRank, text))
    #Delete element if 'rank' < 1
    cursor.execute('DELETE FROM Excuses WHERE text = ? AND rank < 1', (text,))

    #Save changes
    rankDatabaseConnection.commit()
    cursor.close()
    rankDatabaseConnection.close()


create_excuses_db()