from flask import Flask, redirect,request,session,render_template
import os



app = Flask(__name__,static_folder='static')

if __name__ == '__main__':


    @app.route('/', methods=['GET', 'POST'])
    def index():
        form_id = None
        
        if request.method == "POST":
            form_id = request.form.get("form_id")  # Identificar el formulario enviado
            
        if form_id == "loginForm":  # Si el ID del formulario es "loginForm"
            return login()
        elif form_id == "citaForm":  # Si el ID del formulario es "citaForm"
            return new_reserv()
        

        return render_template('index.html')

    def login():
        email = request.form.get("email")
        password = request.form.get("password")

        return f"Correo electronico: {email} \n Contraseña: {password}"


    def new_reserv():
        pass

    try:
        app.run(host='0.0.0.0',port=5050,debug=True)
    except KeyboardInterrupt:
        session.pop('user',None)