from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = '2423415414'

Usuarios_Registrados = {
    'admin@correo.com': {
        'password': 'Admin123',
        'nombre': 'Gio insano',
        'fecha_nacimiento': '2009-11-19'
    }
}

@app.route('/')
def base():
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
        mes = request.form.get('Mes')
        año = request.form.get('Año')

        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('registrar'))


        print(f"Nuevo registro: {nombres} {apellido} - {email}")
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for('inicio'))

    return render_template('Formulario.html')


@app.route('/Validalogin', methods=['POST'])
def Validalogin():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    if not email or not password:
        flash('Por favor ingresa email y contraseña', 'error')


    if email in Usuarios_Registrados:
        usuario = Usuarios_Registrados[email]
        if usuario['password'] == password:
            session['usuario_email'] = email
            session['usuario'] = usuario['nombre']
            session['logueado'] = True
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('base'))
        else:
            flash('Contraseña incorrecta', 'error')
    else:
        flash('Usuario no encontrado', 'error')

    return redirect(url_for('inicio'))


@app.route('/logout')
def logout():
    session.clear()
    flash(f'Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


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

