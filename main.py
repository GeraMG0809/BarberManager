from flask import Flask, redirect, request, session, render_template, url_for,jsonify,flash
from werkzeug.utils import secure_filename
from helpers.user import *
from helpers.citas import *
from helpers.barbero import *
from helpers.servicios import *
from helpers.producto import *
from helpers.venta import *
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)


app = Flask(__name__, static_folder='static')
app.secret_key = 'tu_clave_secreta_segura'  

#-------------------------------------------------------#
#--------------Rutas de pagina de barberia--------------#
#-------------------------------------------------------#


#Ruta principal del index 
@app.route('/', methods=['GET', 'POST'])
def index():
    user = session.get('user')
    form_id = None
    barberos = select_barbers()
    productos = select_productos()


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

    #return render_template('index.html', user=user,barberos = barberos,paquetes = paquetes,productos = productos)
    return render_template('index.html',barberos = barberos,productos= productos,user=user)

#Ruta  de inicio de seesion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password", "").strip()

        error = None

        if not email or not password:
            error = 'Todos los campos son obligatorios'
            return render_template('loginUser.html', error=error)

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

        return render_template('loginUser.html', error=error)

    return render_template('loginUser.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        email = request.form.get("correo_electronico")
        password = request.form.get("password")

        # Validación de campos vacíos
        if not nombre or not telefono or not email or not password:
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for('login'))

        # Verificar si el usuario ya existe
        if select_user_email(email):
            flash("Este correo ya está registrado. Intenta con otro.", "danger")
            return redirect(url_for('login'))     
        
        try:
            # Registrar nuevo usuario
            if new_user(nombre, telefono, email, password):
                # Obtener el usuario recién creado
                user = select_user_email(email)
                if user:
                    user_dict = user.to_dict()
                    # Iniciar sesión
                    session['user'] = user_dict
                    flash("Registro exitoso. ¡Bienvenido!", "success")
                    return redirect(url_for('index'))
                else:
                    flash("Error al obtener los datos del usuario recién creado.", "danger")
                    return redirect(url_for('login'))
            else:
                flash("Error al crear el usuario. Por favor intenta de nuevo.", "danger")
                return redirect(url_for('login'))
        except Exception as e:
            print(f"Error en registro: {str(e)}")
            flash(f"Error interno en el registro: {str(e)}", "danger")
            return redirect(url_for('login'))

    # Si es GET, redirigir a la página de login
    return redirect(url_for('login'))

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


#-------------------------------------------------------#
#-----------------Funciones de barberia-----------------#
#-------------------------------------------------------#

#Funcion de reservacion nueva
def new_reserv():
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")
    barbero = request.form.get("barbero")
    servicio = request.form.get("servicio")

    # Validar si hay sesión iniciada
    user = session.get('user')
    if not user:
        flash("Por favor inicia sesión para hacer una reserva.", "danger")
        return redirect(url_for('login'))
    
    user_id = user.get('id')
    user_phone = user.get('telefono')
    user_name = user.get('name')

    barber_id = select_barbero_id(barbero)
    id_servicio = get_servicio_id(servicio)

    try:
        # Crear la nueva cita
        new_cita(barber_id, user_id, fecha, hora, id_servicio)

        # Enviar confirmación por WhatsApp
        if user_phone and twilio_whatsapp_number:
            message_body = f"¡Hola {user_name}! Tu cita en Barbería Elegante ha sido confirmada para el {fecha} a las {hora} con {barbero} para un {servicio}. ¡Te esperamos!"
            try:
                message = client.messages.create(
                    from_=f'whatsapp:{twilio_whatsapp_number}',
                    body=message_body,
                    to=f'whatsapp:{user_phone}'
                )
                print(f"Mensaje de WhatsApp enviado: {message.sid}")
            except Exception as e:
                print(f"Error al enviar mensaje de WhatsApp: {str(e)}")
                # Considerar cómo manejar este error (ej: loguearlo, notificar al admin)
        else:
            print("Número de teléfono del usuario o número de Twilio no configurado.")

        flash("¡Reserva creada exitosamente!", "success")
        return redirect(url_for('index'))

    except Exception as e:
        print(f"Error al crear la reserva: {str(e)}")
        flash(f"Error al crear la reserva: {str(e)}", "danger")
        return redirect(url_for('index'))

#Funcion para editar valores de usuario
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




#-------------------------------------------------------#
#----------------Rutas de administrador-----------------#
#-------------------------------------------------------#

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    usuario_correcto = 'admin'
    contraseña_correcta = 'admin27'

    if request.method == 'POST':
        user = request.form.get("usuario")
        password = request.form.get("contraseña", "").strip()

        if user == usuario_correcto and password == contraseña_correcta:
            session['admin'] = True  # Marcar al usuario como autenticado
            return redirect(url_for('adminManager'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('admin'))

    return render_template('loginAdmin.html')       

#Funcion principal del administrador 
@app.route('/adminManager')
def adminManager():
    if not session.get('admin'):
        return redirect(url_for('admin'))

    citas = select_citas_pendientes()
    barberos = select_barbers()
    productos = select_productos()

    return render_template('AdminManager.html', citas=citas, barberos=barberos,productos = productos)

@app.route('/barber', methods= ['GET','POST'])
def barber():

    barberos = select_barbers()

    return render_template('barberPage.html', barberos = barberos)


@app.route('/productos',methods = ['GET','POST'])
def productos():

    productos = select_productos()
    return render_template('/productos.html', productos = productos)


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

    return redirect(url_for('barber'))

@app.route('/reportes',methods = ['GET','POST'])
def reportes():
    ventas = select_all_ventas()

    return render_template('venta.html',ventas  = ventas)

from datetime import datetime

@app.route('/crear_venta', methods=['POST'])
def crear_venta():
    try:
        data = request.get_json()
        
        id_cita = data.get('id_cita')
        id_producto = data.get('id_producto')
        tipo_pago = data.get('tipo_pago')
        monto_final = data.get('monto_final')

        if not all([id_cita, id_producto, tipo_pago, monto_final]):
            return jsonify({
                'success': False,
                'message': 'Datos incompletos'
            }), 400

        # Validar que tipo_pago sea válido
        if tipo_pago not in ['Efectivo', 'Tarjeta']:
            return jsonify({
                'success': False,
                'message': 'Tipo de pago inválido'
            }), 400

        # Insertar la venta
        id_venta = insert_venta(
            id_cita=id_cita,
            id_producto=id_producto,
            tipo_pago=tipo_pago,
            monto_final=float(monto_final)
        )

        if not id_venta:
            return jsonify({
                'success': False,
                'message': 'Error al registrar la venta'
            }), 500

        # Actualizar el estado de la cita a FINALIZADA
        if not actualizar_estado_cita(id_cita, 'FINALIZADA'):
            # Si falla la actualización del estado, revertir la venta
            # Aquí podrías agregar lógica para revertir la venta si lo consideras necesario
            return jsonify({
                'success': False,
                'message': 'Error al actualizar el estado de la cita'
            }), 500

        return jsonify({
            'success': True,
            'message': 'Venta registrada y cita finalizada correctamente',
            'id_venta': id_venta
        })
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500




if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5050, debug=True)
    except KeyboardInterrupt:
        session.pop('user', None)
