import sqlite3
db_locale = 'caf.db'
connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
INSERT INTO caf (name, email, carrera, horario)
VALUES ('Juan', 'juan.perez@gmail.com', 'Ingenieria', 'Lunes 18:00')
          """)
connie.commit()
connie.close()
