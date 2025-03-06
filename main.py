from flask import Flask, redirect,request,session,render_template
import os



app = Flask(__name__,static_folder='static')

if __name__ == '__main__':


    @app.route('/')
    def index():
        user = session.get('user')

        return render_template('index.html',user = user)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            print(email)
            print(password)
            return f"Datos recibidos: Email={email}, Password={password}"

        return "Página de inicio - Usa un formulario para enviar datos."        


    try:
        app.run(host='0.0.0.0',port=5050,debug=True)
    except KeyboardInterrupt:
        session.pop('user',None)