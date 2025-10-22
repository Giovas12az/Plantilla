from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '2423415414'  

@app.route('/')
def inicio():
    return render_template('base.html')



@app.route('/Formulario', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellido = request.form.get('apellido')
        email = request.form.get('numero')
        contraseña = request.form.get('pass')  
        confirmarcontraseña = request.form.get('confirm')  
        dia = request.form.get('dia')
        Mes = request.form.get('Mes')
        Año = request.form.get('Año')


        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('Formulario'))

        print(f"Nuevo registro: {nombres} {apellido} - {email}")
        return redirect(url_for('index'))

    return render_template('Formulario.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

if __name__ == '__main__':
    app.run(debug=True)
