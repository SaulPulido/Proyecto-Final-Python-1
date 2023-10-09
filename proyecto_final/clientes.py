import sqlite3
import os
from typing import Any

"""Módulo para la creación de la bases de datos de los clientes"""
class BaseDatos:
    """Se inicializa la clase BaseDatos"""
    def __init__(self, listaClientes):
        self.listaClientes = listaClientes

    def crearBaseDatos(self):
        """Se realiza creación y la conexión hacia la base de datos"""
        try:
            conexion = sqlite3.connect(self.listaClientes)

            """Excepción al error al crear la base de datos"""
        except Exception as e:
            print("Error al crear la Lista de Clientes: {}".format(e))
    
    def verificarListaClientesExiste(self):
        """Verificación de la existencia de la base de datos de los clientes"""
        if os.path.isfile(self.listaClientes):
            return True
        else:
            return False
        
    def crearTablaClientes(self):
        """Creación de la tabla con datos de los clientes"""
        conexion = self.abrirConexion()

        conexion.execute('''CREATE TABLE Lista_Clientes
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         clave TEXT NOT NULL,
                         nombre TEXT NOT NULL,
                         direccion TEXT NOT NULL,
                         correo_electronico TEXT NOT NULL,
                         telefono INTEGER NOT NULL
                         );''')
        
        conexion.close()
    
    def abrirConexion(self):
        """Función para abrir conexión a la base de datos"""
        try:
            conexion = sqlite3.connect(self.listaClientes)

            """retorna la conexión"""
            return conexion
        
            """Excepción al error por no conectar con la base de datos."""
        except Exception as e:
            print("Error al conectar a la Lista de Clientes: {}".format(e))