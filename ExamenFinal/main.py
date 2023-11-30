from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None  # Inicializar la variable antes de la condición

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Lógica de descuento
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        # Cálculos
        total_sin_descuento = tarros * 9000
        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'monto_descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

# EJERCICIO 2
# Datos de usuarios registrados
usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def login():
    mensaje = ""

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificar las credenciales del usuario
        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = "Bienvenido administrador juan"
            elif usuario == 'pepe':
                mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o Contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)