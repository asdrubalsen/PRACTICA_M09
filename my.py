from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

host = "localhost"
user = "Jose Manuel"
password = "JoseManuel"
database = "usuario"
table_name = "nommail"

def connect_db():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

@app.route('/encontrado/<name>')
def encontrado(name):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('SELECT email FROM {} WHERE Nombre = %s'.format(table_name), (name,))
    result = cursor.fetchone()
    db.close()
    if result:
        correo = result[0]
        return '¡Bienvenido ' + name + '!, Tu correo electrónico es: %s' % correo
    else:
        return 'Usuario no encontrado'

@app.route('/getmail', methods=['POST', 'GET'])
def getmail():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('encontrado', name=user))
    else:
        user = request.args.get('name')
        return render_template('getmail.html')

@app.route('/addmail', methods=['GET', 'POST'])
def addmail():
    if request.method == 'POST':
        user = request.form['name']
        email = request.form['email']

        db = connect_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO {} (Nombre, email) VALUES (%s, %s)'.format(table_name), (user, email))
        db.commit()
        db.close()

        return redirect(url_for('encontrado', name=user))
    else:
        return render_template('addmail.html')

if __name__ == '__main__':
    app.run(debug=True)
