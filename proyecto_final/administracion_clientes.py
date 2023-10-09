from clientes import BaseDatos
from autenticacion import Autenticacion
import sqlite3

""" Módulo para la administración de la base de datos de los clientes """
class AdministracionListaClientes:
    """ Clase que contiene el CRUD de la base de datos de los clientes """

    baseDatos = None
    autenticacion = None

    def __init__(self):
        """ Creación de los objetos con respecto a las clases importadas """
        self.baseDatos = BaseDatos('ListaClientes.db')
        self.autenticacion = Autenticacion()

        """ Verificación de la existencia de la base de datos y autenticación con usuario y contraseña """
        if self.baseDatos.verificarListaClientesExiste():
            self.autenticacion.verificarAutenticacion()

            """ En caso de no existir crear la base de datos y la tabla de los clientes """
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablaClientes()

    def mostrarListaClientes(self):
        """ Muestra la lista de los clientes guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Lista_Clientes")
            clientes = cursor.fetchall()

            """ Código condicional para asegurar que existan clientes en la base de datos """
            if len(clientes) > 0:
                print("Lista de clientes actuales: ")
                print("-------------------------------")

                """ Se muestran los datos de cada parámetro de la base de datos """
                for id,clave,nombre,direccion,correo,telefono in clientes:
                    print("ID-Cliente: {},\nClave: {},\nNombre del cliente: {},\nDirección: {},\nCorreo electrónico: {},\nTeléfono: {} \n".format(id,clave,nombre,direccion,correo,telefono))
                print("-------------------------------")
                
                """ En caso de no haber clientes entra la condición negativa """
            else:
                print("No hay clientes en la base de datos")
                print("-------------------------------")

            """ En caso de generar un error por parte de la conexión a la base de datos entra la excepción al error """
        except sqlite3.Error as error:
            print("Error al mostrar el Listado de Clientes", error)

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def agregarCliente(self):
        """ Agrega clientes a la base de datos:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos"""
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()

            """ Se llama la función para ingresar los datos de los clientes con los parámetros de la base de datos y se guardan en una variable: valores """
            clave,nombre,direccion,correo,telefono = self.ingresarDatosCliente()
            valores = (clave,nombre,direccion,correo,telefono)

            """ Se insertan los valores recibidos dentro de cada parámetro de la base de datos """
            sql = ''' INSERT INTO Lista_Clientes(clave,nombre,direccion,correo_electronico,telefono) VALUES (?,?,?,?,?)'''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------")

            """ En caso de generar un error por parte de la conexión y/o en la inserción de los datos entra la excepción al error """
        except sqlite3.Error as e:
            print("Error al intentar insertar los datos: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def modificarCliente(self):
        """ Modifica los datos de un cliente que ya han sido guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Lista_Clientes")
            clientes = cursor.fetchall()

            """ Código condicional para asegurar que existan clientes en la base de datos """
            if len(clientes) > 0:
                print("Lista de clientes para modificar: ")

                """se muestran los clientes actualmente guardados"""
                self.mostrarListaClientes()
                print("-----------------------------")

                """se pide al usuario que introduzca el ID del cliente que desea modificar"""
                id_cliente = self.ingresarID("Ingresa el ID del cliente a modificar: \n")

                """Se selecciona el cliente con el ID que ingresó el usuario"""
                encontrar_cliente = cursor.execute("SELECT * FROM Lista_Clientes WHERE id = ?", (id_cliente,))
                cliente = encontrar_cliente.fetchone()

                """Condicional para asegurar que el cliente se encuentre en la base de datos y se ingresan los nuevos datos del cliente seleccionado"""
                if cliente:
                    clave,nombre,direccion,correo,telefono = self.ingresarDatosCliente()

                    """Se actualizan los datos en la base de datos"""
                    sql = '''UPDATE Lista_Clientes SET clave = ?, nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? WHERE id = ?'''
                    datos_cliente = (clave,nombre,direccion,correo,telefono,id_cliente)
                    cursor.execute(sql, datos_cliente)
                    conexion.commit()
                    print("Datos del cliente modificados correctamente")
                    print("-----------------------------")

                    """En caso de no haber registros con ese ID, se envía un mensaje con esa información"""
                else:
                    print("No hay registro con ese ID")
                    print("-----------------------------")

                """En caso de no haber clientes en la base de datos se envía un mensaje con esa información"""
            else:
                print("No hay clientes para modificar")
                print("-----------------------------")

            """Excepción al error en la modificación del registro"""
        except sqlite3.Error as e:
            print("Error al intentar modificar el registro: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminarClientes(self):
        """ Elimina por completo los datos de un cliente que ya han sido guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Lista_clientes")
            clientes = cursor.fetchall()

            """ Código condicional para asegurar que existan clientes en la base de datos """
            if len(clientes) > 0:
                print("Lista de Clientes para eliminar: ")

                """se muestran los clientes actualmente guardados"""
                self.mostrarListaClientes()
                print("--------------------------------")

                """se pide al usuario que introduzca el ID del cliente que desea modificar"""
                id_cliente = self.ingresarID("Ingresa el ID del cliente a eliminar \n")

                """Se selecciona el cliente con el ID que ingresó el usuario"""
                encontrar_cliente = cursor.execute("SELECT * FROM Lista_Clientes WHERE id = ?", (id_cliente,))

                """Condicional para asegurar que el cliente se encuentre en la base de datos"""
                if len(encontrar_cliente.fetchall()) == 1:

                    """Se borran los datos del cliente en la base de datos y se guarda el cambio"""
                    sql = '''DELETE FROM Lista_Clientes WHERE id = ?'''
                    cursor.execute(sql, (id_cliente,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("--------------------------------")

                    """En caso de no haber registros con ese ID, se envía un mensaje con esa información"""
                else:
                    print("No hay registro con ese ID")
                    print("--------------------------------")

                """En caso de no haber clientes en la base de datos se envía un mensaje con esa información"""
            else:
                print("No hay clientes para eliminar")
                print("--------------------------------")

            """Excepción al error en la eliminación del registro"""
        except sqlite3.Error as e:
            print("Error al intentar eliminar el registro: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def ingresarID(self,mensaje):
        """Función para ingresar el ID de un registro existente en la base de datos y realizar algun cambio en la información de ese cliente o su eliminación"""
        id_cliente = 0
        datos_incorrectos = True

        """Bucle y bloque de sentencias con excepciones para pedir que el usuario introduzca el ID del cliente"""
        while datos_incorrectos:

            """Entrada del input y terminación del bucle while"""
            try:
                id_cliente = int(input( mensaje ))
                datos_incorrectos = False

                """Excepción en caso de haber error al capturar el ID del cliente y continuación del bucle while"""
            except Exception as e:
                print("Error al capturar el ID del cliente: {}".format(e))
                print("Intente de nuevo ingresar el ID \n")
                datos_incorrectos = True

            """Retorna el id del cliente"""
        return id_cliente

    def ingresarDatosCliente(self):
        """Función para ingresar los datos del cliente y realizar algún registro nuevo o cambio en la información actual"""
        datos_incorrectos = True

        """Bucle y bloque de excepciones para ingresar los datos solicitados por la base de datos"""
        while datos_incorrectos:
            try:
                clave = input("Ingresa la clave del cliente: \n")
                nombre = input("Ingresa el nombre del cliente: \n")
                direccion = input("Ingresa la dirección del cliente: \n")
                correo_electronico = input("Ingresa el correo electrónico del cliente: \n")
                telefono = int(input("Ingresa el teléfono del cliente: \n"))

                """Se termina el bucle while"""
                datos_incorrectos = False

                """Excepcion en caso de haber un error al capturar un dato"""
            except Exception as e:
                print("Error al capturar un dato: {}".format(e))
                print("Intente de nuevo ingresar los datos \n")
                datos_incorrectos = True

                """Retorna los datos escritos por el usuario"""
        return clave,nombre,direccion,correo_electronico,telefono