from flask import Flask, render_template
import sqlite3

"""Módulo para correr flask y mostrar en un html la lista de los pedidos"""
app = Flask(__name__, template_folder="templates")

"""Ruta principal del aplicativo"""
@app.route('/')
def index():
    """Definición de las variables ubicadas en el template"""
    encabezado_pagina = "Pedidos"
    titulo_pagina = "Lista de pedidos"

    """Se realiza la conexión a la base de datos"""
    conexion = sqlite3.connect("Pedidos.db")

    """Se seleccionan los datos de la tabla Pedidos"""
    cursor = conexion.execute("SELECT * FROM Pedidos")
    pedidos = cursor.fetchall()

    """Retorna el renderizado en el archivo index.html con las variables y los datos de la tabla Pedidos """
    return render_template("index.html", 
                           encabezado_pagina = encabezado_pagina,
                           titulo_pagina = titulo_pagina,
                           pedidos = pedidos)
    