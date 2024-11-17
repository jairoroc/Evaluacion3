from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
        return render_template('index.html')


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        try:

            nota1 = int(request.form["nota1"])
            nota2 = int(request.form["nota2"])
            nota3 = int(request.form["nota3"])
            asistencia = int(request.form["asistencia"])


            promedio = (nota1 + nota2 + nota3) / 3


            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"


            resultado = {
                "promedio": f"{promedio:.1f}",
                "estado": estado
            }

        except ValueError:
            resultado = {
                "promedio": "Error",
                "estado": "Por favor, ingresar un valor numérico válido."
            }


    return render_template("ejercicio1.html", resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = ""
    longitud_mayor = 0

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        # Encontrar el nombre más largo
        nombre_mayor = max(nombres, key=len)
        longitud_mayor = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, longitud_mayor=longitud_mayor)



if __name__ == "__main__":
    app.run(debug=True)