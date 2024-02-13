from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista que asocia nombres de usuario con correos electrónicos
usuarios_correos = {
"Mercedes" :	"mcast386@xtec.cat",
"Rayane":	"rayane@rayane.sa",
"Mohamed":	"moha@gmail.com",
"Jad":	"jad@gmail.com",
"Oriol":	"joam@gmail.com",
"Elias":	"hola123@gmail.com",
"Armau":	"arnau@gmail.com",
"Asdrúbal":	"asdrubal@gmail.com",
"Adrian":	"pedrosanchez@asix2.com",
"Eric": 	"eric@gmail.com",
"Emma":	"pacosanz@gmail.com",
"nishwan2":	"nishwan@gmail.com",
"Javi":	"javi@gmail.com",
"Novel":	"novelferreras49@gmail.com",
"Bruno":	"elcigala@gmail.com",
"David":	"argentino@gmail.com",
"Judit":	"judit@gmail.com",
"Joao":	"joao@gmail.com",
"Laura":	"laura@gmail.com",
"enrico":	"123@gmail.com",
"Joel":	"joelcobre@gmail.com",
"Aaron":	"aaron@gmail.com",
"Moad":	"moad@gmail.com",
"peruano":	"peru@gmail.com"}

@app.route('/encontrado/<name>')
def encontrado(name):
    # Verificar si el nombre de usuario existe en la lista
    if name in usuarios_correos:
        correo = usuarios_correos[name]
        return '¡Bienvenido '  + name + '!, Tu correo electrónico es: %s' % correo
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

        # Actualizar la lista usuarios_correos con los nuevos datos
        usuarios_correos.update({user: email})

        return redirect(url_for('encontrado', name=user, email=email))
    else:
        return render_template('addmail.html')

if __name__ == '__main__':
    app.run(debug=True)
