from flask import Flask, redirect,request,session,render_template
import os



app = Flask(__name__,static_folder='static')

if __name__ == '__main__':


    @app.route('/', methods=['GET', 'POST'])
    def index():
        
        if request.method == 'POST':
            if "login" in request.form:
                return login()
            elif "cita" in request.form:
                return new_reserv()
        
        return render_template('index.html')

    def login():
        email = request.form.get("email")
        password = request.form.get("password")

        print(f"Correo electronico: {email} \n Contraseña: {password}")


    def new_reserv():
        pass

    try:
        app.run(host='0.0.0.0',port=5050,debug=True)
    except KeyboardInterrupt:
        session.pop('user',None)