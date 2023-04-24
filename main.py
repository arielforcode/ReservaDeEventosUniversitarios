from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app =Flask(__name__)

##---------------- configuracion de flask para la base de datos ------------------
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Iselva1290'
app.config['MYSQL_DB']='proyecto'
mysql = MySQL(app)
## -------------------------------------------------------------------------------

@app.route('/')
def Index():
    return render_template('Index.html')

## ------------------------- Login validator -----------------------------------
@app.route('/LoginPage')
def LoginPage():
    return render_template('Login.html')


@app.route('/Login',methods=['POST'])
def Login():
    if request.method == 'POST':
        email= request.form['correo'].strip()
        password = request.form ['password']
        if(email=="ariel@gmail.com" and password == "12345678"):
            return redirect(url_for('MainAdministrador'))
        elif(email== "prueba@gmail.com"):
            return redirect(url_for('Participante'))
        else:
            return redirect(url_for('LoginPage'))

# ------------------------------------------------------------------------------
# --------------------Administrador --------------------------------
@app.route('/MainAdministrador')
def MainAdministrador():
    return render_template('/Control/Administrador.html')

@app.route('/AdministrarUsuarios')
def AdministrarUsuarios():
    return render_template('/Control/AdministrarUsuarios.html')

@app.route('/AdministrarEventos')
def AdministrarEventos():
    return render_template('/Control/AdministrarEventos.html')

@app.route('/AdministrarLanding')
def AdministrarLanding():
    return render_template('/Control/AdministrarLanding.html')
# ------------------------------------------------------------------
#------------------ Participante -----------------------------------------

@app.route('/Participante')
def Participante():
    return render_template('/Participante/Participante.html')

#-------------------------------------------------------------------------
@app.route('/User')
def User():
    print("hiciste clic en usuario")
    return render_template('/Control/Usuario.html')

if __name__ == '__main__':
    app.run(port=3000,debug=True)