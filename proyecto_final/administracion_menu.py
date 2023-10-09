from menu import BaseDatosM
import sqlite3

""" Módulo para la administración de la base de datos del Menú """
class AdministracionMenu:
    """ Clase que contiene el CRUD de la base de datos de los clientes """

    baseDatos = None

    def __init__(self):
        """ Creación del objeto con respecto a la clase importada """
        self.baseDatos = BaseDatosM('Menu.db')

        """ Verificación de la existencia de la base de datos """
        if self.baseDatos.verificarMenuExiste():
            print("¡Entrando al Menú de Happy Burger!")

            """ En caso de no existir crear la base de datos y la tabla del menú """
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearMenu()

    def mostrarMenu(self):
        """ Muestra la lista de los clientes guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Menu")
            productos = cursor.fetchall()

            """ Código condicional para asegurar que existan productos en la base de datos """
            if len(productos) > 0:
                print("Lista de productos actuales: ")
                print("-------------------------------")

                """ Se muestran los datos de cada parámetro de la base de datos """
                for id,clave,nombre,precio in productos:
                    print("ID-Producto: {},\nClave: {},\nNombre del producto: {},\nPrecio del producto: {}\n".format(id,clave,nombre,precio))
                print("-------------------------------")

                """ En caso de no haber productos entra la condición negativa """
            else:
                print("No hay productos en el Menú")
                print("-------------------------------")

            """ En caso de generar un error por parte de la conexión a la base de datos entra la excepción al error """
        except sqlite3.Error as error:
            print("Error al mostrar el Menú", error)

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def agregarProducto(self):
        """ Agrega productos a la base de datos:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos"""
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()

            """ Se llama la función para ingresar los datos de los productos con los parámetros de la base de datos y se guardan en una variable: valores """
            clave,nombre,precio = self.ingresarDatosProducto()
            valores = (clave,nombre,precio)

            """ Se insertan los valores recibidos dentro de cada parámetro de la base de datos """
            sql = ''' INSERT INTO Menu(clave,nombre,precio) VALUES (?,?,?)'''
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

    def modificarProducto(self):
        """ Modifica los datos de un producto que ya han sido guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Menu")
            productos = cursor.fetchall()

            """ Código condicional para asegurar que existan productos en la base de datos """
            if len(productos) > 0:
                print("Lista de productos para modificar: ")

                """se muestran los productos actualmente guardados"""
                self.mostrarMenu()
                print("-----------------------------")

                """se pide al usuario que introduzca el ID del producto que desea modificar"""
                id_producto = self.ingresarID("Ingresa el ID del producto a modificar: \n")

                """Se selecciona el productos con el ID que ingresó el usuario"""
                encontrar_producto = cursor.execute("SELECT * FROM Menu WHERE id = ?", (id_producto,))
                producto = encontrar_producto.fetchone()

                """Condicional para asegurar que el productos se encuentre en la base de datos y se ingresan los nuevos datos del producto seleccionado"""
                if producto:
                    clave,nombre,precio = self.ingresarDatosProducto()

                    """Se actualizan los datos en la base de datos"""
                    sql = '''UPDATE Menu SET clave = ?, nombre = ?, precio = ? WHERE id = ?'''
                    datos_producto = (clave,nombre,precio,id_producto)
                    cursor.execute(sql, datos_producto)
                    conexion.commit()
                    print("Datos del producto modificados correctamente")
                    print("-----------------------------")

                    """En caso de no haber registros con ese ID, se envía un mensaje con esa información"""
                else:
                    print("No hay registro con ese ID")
                    print("-----------------------------")

                """En caso de no haber clientes en la base de datos se envía un mensaje con esa información"""
            else:
                print("No hay productos para modificar")
                print("-----------------------------")

            """Excepción al error en la modificación del registro"""
        except sqlite3.Error as e:
            print("Error al intentar modificar el producto: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminarProductos(self):
        """ Elimina por completo los datos de un producto que ya han sido guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Menu")
            productos = cursor.fetchall()

            """ Código condicional para asegurar que existan productos en la base de datos """
            if len(productos) > 0:
                print("Lista de productos para eliminar: ")

                """se muestran los productos actualmente guardados"""
                self.mostrarMenu()
                print("--------------------------------")

                """se pide al usuario que introduzca el ID del producto que desea modificar"""
                id_producto = self.ingresarID("Ingresa el ID del producto a eliminar \n")

                """Se selecciona el producto con el ID que ingresó el usuario"""
                encontrar_producto = cursor.execute("SELECT * FROM Menu WHERE id = ?", (id_producto,))

                """Condicional para asegurar que el producto se encuentre en la base de datos"""
                if len(encontrar_producto.fetchall()) == 1:

                    """Se borran los datos del producto en la base de datos y se guarda el cambio"""
                    sql = '''DELETE FROM Menu WHERE id = ?'''
                    cursor.execute(sql, (id_producto,))
                    conexion.commit()
                    print("Registro eliminado correctamente")
                    print("--------------------------------")

                    """En caso de no haber registros con ese ID, se envía un mensaje con esa información"""
                else:
                    print("No hay registro con ese ID")
                    print("--------------------------------")

                """En caso de no haber clientes en la base de datos se envía un mensaje con esa información"""
            else:
                print("No hay productos para eliminar")
                print("--------------------------------")

            """Excepción al error en la eliminación del registro"""
        except sqlite3.Error as e:
            print("Error al intentar eliminar el producto: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def ingresarID(self,mensaje):
        """Función para ingresar el ID de un registro existente en la base de datos y realizar algun cambio en la información de ese producto o su eliminación"""
        id_producto = 0
        datos_incorrectos = True

        """Bucle y bloque de sentencias con excepciones para pedir que el usuario introduzca el ID del producto"""
        while datos_incorrectos:

            """Entrada del input y terminación del bucle while"""
            try:
                id_producto = int(input( mensaje ))
                datos_incorrectos = False

                """Excepción en caso de haber error al capturar el ID del producto y continuación del bucle while"""
            except Exception as e:
                print("Error al capturar el ID del producto: {}".format(e))
                print("Intente de nuevo ingresar el ID \n")
                datos_incorrectos = True

            """Retorna el id del cliente"""
        return id_producto

    def ingresarDatosProducto(self):
        """Función para ingresar los datos del producto y realizar algún registro nuevo o cambio en la información actual"""
        datos_incorrectos = True

        """Bucle y bloque de excepciones para ingresar los datos solicitados por la base de datos"""
        while datos_incorrectos:
            try:
                clave = input("Ingresa la clave del producto: \n")
                nombre = input("Ingresa el nombre del producto: \n")
                precio = float(input("Ingresa el precio del producto: \n"))

                """Se termina el bucle while"""
                datos_incorrectos = False

                """Excepcion en caso de haber un error al capturar un dato"""
            except Exception as e:
                print("Error al capturar un dato: {}".format(e))
                print("Intente de nuevo ingresar los datos \n")
                datos_incorrectos = True

                """Retorna los datos escritos por el usuario"""
        return clave,nombre,precio