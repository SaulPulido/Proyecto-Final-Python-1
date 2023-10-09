import sqlite3
import os
from typing import Any

"""Módulo para la creación de la bases de datos del menú"""
class BaseDatosM:
    """Se inicializa la clase BaseDatos"""
    def __init__(self, menu):
        self.menu = menu

    def crearBaseDatos(self):
        """Se realiza creación y la conexión hacia la base de datos"""
        try:
            conexion = sqlite3.connect(self.menu)

            """Excepción al error al crear la base de datos"""
        except Exception as e:
            print("Error al crear el Menú: {}".format(e))
    
    def verificarMenuExiste(self):
        """Verificación de la existencia de la base de datos del menú"""
        if os.path.isfile(self.menu):
            return True
        else:
            return False
        
    def crearMenu(self):
        """Creación de la tabla con datos de los productos del menú"""
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE Menu
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         clave TEXT NOT NULL,
                         nombre TEXT NOT NULL,
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
            print("Error al abrir el Menú: {}".format(e))