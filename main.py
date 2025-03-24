from flask import Flask, redirect, request, session, render_template, url_for
from helpers.user import *

app = Flask(__name__, static_folder='static')
app.secret_key = 'tu_clave_secreta_segura'  

@app.route('/', methods=['GET', 'POST'])
def index():
    user = session.get('user')
    form_id = None

    if request.method == "POST":
        form_id = request.form.get("form_id")  
        
    if form_id == "loginForm":
        return login()
    elif form_id == "signupForm":
        return register()
    elif form_id == "bookingForm":
        return new_reserv()

    return render_template('index.html', user=user)


def login():
    email = request.form.get("email")
    password = request.form.get("password").strip()  

    error = None
    user = select_user_email(email)  # Función que obtiene el usuario de la base de datos

    if user:
        stored_password = str(user.password).strip()  
        if stored_password == password:
            session['user'] = user.to_dict()  
            return redirect('/') 
        else:
            error = 'Correo electrónico o contraseña inválidos'
    else:
        error = 'Usuario no encontrado'

    return render_template('index.html', error=error)


def register():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    email = request.form.get("correo_electronico")
    password = request.form.get("password")

    new_user(nombre, telefono, email, password)

    return f"Nombre: {nombre}\nTeléfono: {telefono}\nCorreo electrónico: {email}\nContraseña: {password}"


def new_reserv():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")
    barbero = request.form.get("barbero")
    servicio = request.form.get("servicio")

    return f"NOMBRE: {nombre} TELEFONO: {telefono} FECHA:{fecha} HORA: {hora} BARBERO: {barbero} SERVICIO: {servicio} "


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5050, debug=True)
    except KeyboardInterrupt:
        session.pop('user', None)
