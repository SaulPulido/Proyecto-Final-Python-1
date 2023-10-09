import sqlite3
import os
from typing import Any

"""Módulo para la creación de la bases de datos de los pedidos"""
class BaseDatosP:
    """Se inicializa la clase BaseDatos"""
    def __init__(self, menu):
        self.menu = menu

    def crearBaseDatos(self):
        """Se realiza creación y la conexión hacia la base de datos"""
        try:
            conexion = sqlite3.connect(self.menu)

            """Excepción al error al crear la base de datos"""
        except Exception as e:
            print("Error al crear el registro de Pedidos: {}".format(e))
    
    def verificarPedidosExiste(self):
        """Verificación de la existencia de la base de datos de los pedidos"""
        if os.path.isfile(self.menu):
            return True
        else:
            return False
        
    def crearPedidos(self):
        """Creación de la tabla con datos de los pedidos"""
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE Pedidos
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         pedido INTEGER NOT NULL,
                         cliente TEXT NOT NULL,
                         producto TEXT NOT NULL,
                         precio FLOAT NOT NULL
                         );''')
        
        conexion.close()
    
    def abrirConexion(self):
        """Función para abrir conexión a la base de datos"""
        try:
            conexion = sqlite3.connect(self.menu)

            """retorna la conexión"""
            return conexion
        
            """Excepción al error por no conectar con la base de datos."""
        except Exception as e:
            print("Error al abrir los Pedidos: {}".format(e))