import sqlite3

db_locale = 'caf.db'

def check_tables():
    connie = sqlite3.connect(db_locale)
    c = connie.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='caf';")
    tables = c.fetchall()
    connie.close()
    return tables

if __name__ == '__main__':
    tables = check_tables()
    if tables:
        print("La tabla 'caf' existe:", tables)
    else:
        print("La tabla 'caf' no existe.")