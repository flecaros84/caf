from flask import Flask, render_template,url_for,request
import sqlite3
app = Flask(__name__)
db_locale = 'caf.db'

#Render del home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#Render del formulario
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        user_details =(
            request.form['name'],
            request.form['email'],
            request.form['carrera'],
            request.form['horario']
        )
        insert_comments(user_details)
        return render_template('success.html')

#Función para insertar los datos en la base de datos
def insert_comments(user_details):
    connie = sqlite3.connect(db_locale)
    c=connie.cursor()
    sql_execute_string = 'INSERT INTO caf (name, email, carrera, horario) VALUES (?,?,?,?)';
    c.execute(sql_execute_string, user_details)
    connie.commit()
    connie.close()

#Función para consultar los datos de la base de datos
def query_comments():
    connie = sqlite3.connect(db_locale)
    c=connie.cursor()
    c.execute("""
        SELECT * FROM caf
    """)
    userdata = c.fetchall()
    connie.close()
    return userdata

#Render de la página de administrador
@app.route('/admin')
def admin():
    user_data = query_comments()
    return render_template('admin.html',user_data=user_data)

if __name__ =='__main__':
    app.run(debug=True)

