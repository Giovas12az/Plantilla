from flask import Flask, render_template,request,redirect,url_for,flash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def base():
    return render_template("base.html")

@app.route('/Formulario')
def base1():
    return render_template("Formulario.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/Tindex')
def Tindex():
    return render_template("Tindex.html")

@app.route('/animales')
def animales():
    return render_template("animales.html")

@app.route('/vehiculos')
def vehiculos():
    return render_template("vehiculos.html")

@app.route('/maravillas')
def maravillas():
    return render_template("maravillas.html")

@app.route('/acerca')
def acerca():
    return render_template("acerca.html")

@app.route('/registrame', methods=['GET', 'POST'])
def registrame():
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('correo')
        dia = request.form.get('dia')
        Año = request.form.get('Año')
        Mes = request.form.get('Mes')
        contraseña = request.form.get('contraseña')
        genero = request.form.get('genero')  

        # Validaciones
        if not nombre:
            error = 'El nombre es obligatorio'
        elif not apellido:
            error = 'El apellido es obligatorio'
        elif not correo:
            error = 'El correo es obligatorio'
        elif not dia:
            error = 'El día es obligatorio'
        elif not Mes:
            error = 'El mes es obligatorio'
        elif not Año:
            error = 'El año es obligatorio'
        elif not genero:
            error = 'El género es obligatorio'
        elif not contraseña:
            error = 'La contraseña es obligatoria'

        if error:
            flash(error)
        
            return render_template('formulario.html')
        else:
            flash(f"Registrado correctamente, {nombre}")
            return redirect(url_for('registrame'))  

    return render_template('formulario.html')

if __name__=="__main__":
    app.run(debug=True)
