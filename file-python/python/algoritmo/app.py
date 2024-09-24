from flask import Flask, render_template, request
import random

app = Flask(__name__)

def clave_binaria(longitud):
    bts = [random.choice(['0', '1']) for _ in range(longitud)]
    clave = ''.join(bts)
    return clave

@app.route('/', methods=['GET', 'POST'])
def index():
    clave_generada = None
    if request.method == 'POST':
        try:
            longitud = int(request.form['longitud'])
            if longitud > 0:
                clave_generada = clave_binaria(longitud)
            else:
                clave_generada = "Error: Ingrese un número positivo"
        except ValueError:
            clave_generada = "Error: Ingrese un número entero válido"
    
    return render_template('index.html', clave=clave_generada)

if __name__ == '__main__':
    app.run(debug=True)