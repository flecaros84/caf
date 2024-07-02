import sqlite3
db_locale = 'caf.db'
connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
SELECT * FROM caf
          """)
user_info= c.fetchall()
print(user_info)
connie.commit()
connie.close()
