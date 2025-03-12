from flask import Flask, redirect, request, session, render_template

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    form_id = None
    
    if request.method == "POST":
        form_id = request.form.get("form_id")  # Identificar el formulario enviado
        
    if form_id == "loginForm":
        return login()
    elif form_id == "signupForm":
        return register()
    elif form_id == "citaForm":
        return new_reserv()

    return render_template('index.html')

def login():
    email = request.form.get("email")
    password = request.form.get("password")

    return f"Correo electrónico: {email}\nContraseña: {password}"

def register():
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    email = request.form.get("correo_electronico")
    password = request.form.get("password")  

    return f"Nombre: {nombre}\nTeléfono: {telefono}\nCorreo electrónico: {email}\nContraseña: {password}"

def new_reserv():
    return "Función de nueva reserva"

if __name__ == '__main__':  #
    try:
        app.run(host='0.0.0.0', port=5050, debug=True)
    except KeyboardInterrupt:
        session.pop('user', None)
