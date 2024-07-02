import sqlite3
db_locale = 'caf.db'
connie = sqlite3.connect(db_locale)
c = connie.cursor()

#Creación de la base de datos
c.execute("""CREATE TABLE caf
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          email TEXT,
          carrera TEXT,
          horario TEXT)
          """)

connie.commit()
connie.close()
