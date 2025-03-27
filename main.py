from flask import Flask, redirect, request, session, render_template, url_for,jsonify
from helpers.user import *
from helpers.citas import *
from helpers.barbero import *
from helpers.servicios import *
from datetime import datetime



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
    
    #horario_libre = horarios_disponibles()

    return render_template('index.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index')) 


@app.route('/horarios_disponibles', methods=['GET'])
def horarios_disponibles():
    barbero = request.args.get("barbero")
    fecha = request.args.get("fecha")

    if not barbero or not fecha:
        return jsonify({"error": "Faltan parámetros"}), 400

    id_barbero = select_barbero_id(barbero)

    if id_barbero is None:
        return jsonify({"error": "Barbero no encontrado"}), 404  # Evita consultas incorrectas

    horarios = obtener_horarios_disponibles(id_barbero, fecha)

    return jsonify(horarios)



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

    

    user_id = session.get('user')['id']
    barber_id = select_barbero_id(barbero)
    format_fecha = datetime.strptime(fecha,"%y-%m-%d").strftime("%d/5m/%y")
    id_servicio = get_servicio_id(servicio)

    #new_cita(barber_id,user_id,format_fecha,hora,id_servicio)   


    return f"NOMBRE: {nombre} TELEFONO: {telefono} FECHA:{fecha} HORA: {hora} BARBERO: {barbero} SERVICIO: {servicio} "


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5050, debug=True)
    except KeyboardInterrupt:
        session.pop('user', None)
