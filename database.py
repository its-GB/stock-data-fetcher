import sqlite3

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stock_data
                 (Date TEXT, Company TEXT, Open REAL, Close REAL, High REAL, Low REAL, Volume INTEGER)''')
    return conn, c

def insert_data(c, data):
    c.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?)", data)

def commit_and_close(conn):
    conn.commit()
    conn.close()
