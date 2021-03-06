#Nombre: Jhostyn Javier Gavilanez Suarez 

# Se importan las librerias necesarias para trabajar con el framwork Flask
from flask import Flask, render_template

# Se crea la aplicacion, y se pasa como parametro el nombre de la aplicacion y el nombre de la carpeta donde se encuentra el archivo html
app = Flask(__name__, template_folder='template')

# controlador  ruta para la pagina principal
@app.route('/')
def principal():
    # Se retorna el archivo html principal
    return render_template('index.html')



# Se ejeuta la aplicacion en modo debug, esto para que se pueda ver los cambios en el codigo sin necesidad de reiniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)