from flask import Flask, redirect, request, session, render_template, url_for,jsonify,flash
from werkzeug.utils import secure_filename
from helpers.user import *
from helpers.citas import *
from helpers.barbero import *
from helpers.servicios import *
import os



app = Flask(__name__, static_folder='static')
app.secret_key = 'tu_clave_secreta_segura'  

@app.route('/', methods=['GET', 'POST'])
def index():
    user = session.get('user')
    form_id = None
    barberos = select_barbers()

    if request.method == "POST":
        form_id = request.form.get("form_id")        
        if form_id == "loginForm":
            return login()
        elif form_id == "signupForm":
            return register()
        elif form_id == "bookingForm":
            return new_reserv()
        elif form_id == "editUserForm":
            return edit_user()

    return render_template('index.html', user=user,barberos = barberos)

@app.route('/admin')
def admin():

    citas = select_citas_pendientes()
    barberos = select_barbers()
    return render_template('AdminManager.html', citas = citas, barberos = barberos)


@app.route('/agregar_barbero', methods=['POST'])
def agregar_barbero():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    imagen = request.files['imagen']
    
    if imagen:
        filename = secure_filename(imagen.filename)
        ruta_imagen = os.path.join('static', 'imges', filename)
        
        # Crear carpeta si no existe
        os.makedirs(os.path.dirname(ruta_imagen), exist_ok=True)
        
        imagen.save(ruta_imagen)

        # Insertar en base de datos
        insert_barbero(nombre, telefono, filename)  # solo guardamos el nombre del archivo

    return redirect(url_for('admin'))

#Ruta  de inicio de seesion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password", "").strip()

        error = None

        if not email or not password:
            error = 'Todos los campos son obligatorios'
            return render_template('index.html', error=error, show_login_modal=True)

        user = select_user_email(email)

        if user:
            stored_password = str(user.password).strip()
            if stored_password == password:
                session['user'] = user.to_dict()
                return redirect('/')
            else:
                error = 'Correo electrónico o contraseña inválidos'
        else:
            error = 'Usuario no encontrado'

        print("Error:", error)

        return render_template('index.html', error=error, show_login_modal=True)

    return render_template('index.html')




#Funcion de registro de usuarios
def register():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    email = request.form.get("correo_electronico")
    password = request.form.get("password")

    # Validación de campos vacíos (opcional pero recomendado)
    if not nombre or not telefono or not email or not password:
        flash("Todos los campos son obligatorios", "warning")
        return redirect('/registro')

    # Verificar si el usuario ya existe
    if select_user_email(email):
        flash("Este correo ya está registrado. Intenta con otro.", "danger")
        return redirect('/registro')
    
    # Registrar nuevo usuario
    new_user(nombre, telefono, email, password)

    # Obtener el usuario recién creado (puedes usar select_user_email)
    user = select_user_email(email)

    # Iniciar sesión
    session['user_id'] = user['id']  # Asegúrate de que 'id' esté en la consulta
    session['user_name'] = user['nombre']

    flash("Registro exitoso. ¡Bienvenido!", "success")
    return redirect('/index')  # O render_template('index.html')

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


def new_reserv():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")
    barbero = request.form.get("barbero")
    servicio = request.form.get("servicio")

    # Validar si hay sesión iniciada
    user = session.get('user')
    if not user:
        return jsonify({
            "error": "Usuario no autenticado",
            "status": 401
        }), 401  # Código de error HTTP 401 (No autorizado)

    user_id = user.get('id')
    barber_id = select_barbero_id(barbero)

    # Corregir formato de la fecha
    id_servicio = get_servicio_id(servicio)

    new_cita(barber_id,user_id,fecha,hora,id_servicio)   
    return jsonify({
            "status": "success",
            "message": "Reserva creada correctamente",
            "reserva": {
                "nombre": nombre,
                "telefono": telefono,
                "fecha": fecha,
                "hora": hora,
                "barbero": barber_id,
                "servicio": id_servicio,
                "user_id": user_id
            }
        }), 200

def edit_user():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")

    user = session.get('user')
    user_id = user.get('id')
    modify_user(user_id,nombre,telefono)

    return jsonify({
        "status":"succes",
        "message":"Modificacion de datos correcta",
        "datos": {
            "user_id":user_id,
            "nombre":nombre,
            "telefono":telefono
        }
    }),2000


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5050, debug=True)
    except KeyboardInterrupt:
        session.pop('user', None)
