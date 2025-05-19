import sqlite3
from sqlite3 import Cursor, Connection
import os

rankDatabasePath = 'src/models/bd/excuses_ranks.db'

#Create DB if not exist
def create_excuses_db():
    #Create folder for DB if not exist
    try:
        os.mkdir("src/models/bd")
    except FileExistsError:
        ...
    #Connect to DB
    rankDatabaseConnection = sqlite3.connect(rankDatabasePath)
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
def add_excuse(text: str, cursor: Cursor = None):
    databaseConnection = None
    if cursor == None:
        databaseConnection, cursor = connect_to_db(rankDatabasePath)
    #Check if element not already exsist
    if (not check_if_exist(text, cursor)):
        #Find max id
        result_max_id = cursor.execute('SELECT MAX(id) FROM Excuses').fetchone()
        if(result_max_id[0] is not None):
            id = result_max_id[0] + 1
        else:
            id = 1

        #Insert new element
        cursor.execute('INSERT INTO Excuses (id, text, rank) VALUES (?, ?, ?)', (id, text, 0))
        print(f"ID = {id}")

        disconnect_from_db(databaseConnection, cursor)
        return id

#Change 'rank' in BD and delete element if 'rank' < 0
def change_rank(id: int, deltaRank: int):
    #Return if trying to change rank more then one. Need it to further protection
    if(abs(deltaRank) > 1):
        return 
    #Connect to DB
    rankDatabaseConnection, cursor = connect_to_db(rankDatabasePath)

    #Try to add element : OUTDATED. No more reason, elements add to db when /generate-joke is called
    #add_excuse(text, cursor)
    #Update'rank'
    cursor.execute('UPDATE Excuses SET rank = rank + ? WHERE id = ?', (deltaRank, id))
    #Delete element if 'rank' < 0
    cursor.execute('DELETE FROM Excuses WHERE id = ? AND rank < 0', (id,))

    #Save changes
    disconnect_from_db(rankDatabaseConnection, cursor)

#Get certian amount of Excuses from DB
def get_excuses(numberOfExcuses: int, needAll: bool = False):
    #Connect to DB
    rankDatabaseConnection, cursor = connect_to_db(rankDatabasePath)
    #Get values
    if needAll:
        cursor.execute('SELECT * FROM Excuses WHERE rank >= 0')
    else:
        cursor.execute('SELECT * FROM Excuses WHERE rank >= 0 ORDER BY rank DESC LIMIT ?', (numberOfExcuses,))
    results = cursor.fetchall()
    
    print(results)

    #Disconnect from DB
    disconnect_from_db(rankDatabaseConnection, cursor)
    #Return results
    return results

#Connect to database
def connect_to_db(path: str):
    databaseConnection = sqlite3.connect(path)
    cursor = databaseConnection.cursor()

    return databaseConnection, cursor

#Disconnect from database
def disconnect_from_db(databaseConnection: Connection, cursor: Cursor):
    databaseConnection.commit()
    cursor.close()
    databaseConnection.close()    

create_excuses_db()