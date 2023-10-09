from pedido import BaseDatosP
import sqlite3

""" Módulo para la administración de la base de datos de los pedidos """
class AdministracionPedido:
    """ Clase que contiene la creación y eliminación de la base de datos de los pedidos """

    baseDatos = None

    def __init__(self):
        """ Creación del objeto con respecto a la clase importada """
        self.baseDatos = BaseDatosP('Pedidos.db')

        """ Verificación de la existencia de la base de datos"""
        if self.baseDatos.verificarPedidosExiste():
            print("Entrando al Registro de Pedidos")

            """ En caso de no existir crear la base de datos y la tabla de los clientes """
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearPedidos()

    def mostrarPedidos(self):
        """ Muestra la lista de los pedidos guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Pedidos")
            pedidos = cursor.fetchall()

            """ Código condicional para asegurar que existan pedidos en la base de datos """
            if len(pedidos) > 0:
                print("Lista de pedidos actuales: ")
                print("-------------------------------")

                """ Se muestran los datos de cada parámetro de la base de datos """
                for id,pedido,cliente,producto,precio in pedidos:
                    print("ID-Producto: {},\nPedidoN°: {},\nCliente: {},\nNombre del producto: {},\nPrecio del producto: {}\n".format(id,pedido,cliente,producto,precio))
                print("-------------------------------")

                """ En caso de no haber pedidos entra la condición negativa """
            else:
                print("No hay pedidos en el Registro")
                print("-------------------------------")

            """ En caso de generar un error por parte de la conexión a la base de datos entra la excepción al error """
        except sqlite3.Error as error:
            print("Error al mostrar los Pedidos", error)

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def agregarPedido(self):
        """ Agrega pedidos a la base de datos:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos"""
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()

            """ Se llama la función para ingresar los datos de los pedidos con los parámetros de la base de datos y se guardan en una variable: valores """
            pedido,cliente,producto,precio = self.ingresarDatosPedido()
            valores = (pedido,cliente,producto,precio)

            """ Se insertan los valores recibidos dentro de cada parámetro de la base de datos """
            sql = ''' INSERT INTO Pedidos(pedido,cliente,producto,precio) VALUES (?,?,?,?)'''
            cursor.execute(sql,valores)
            conexion.commit()
            print("Pedido guardado correctamente")
            print("Imprimiendo ticket")
            print("------------------------------\n")

            """Se genera el ticket creando un archivo .txt con la información del pedido"""
            ticketW = open("ticket.txt", "w")
            ticketW.write("\tHappy Burger S.A. de C.V.\n\n"
                  "Producto: " +producto +" .......... $" + str(precio) + " pesos\n"
                  " Total a pagar: $" + str(precio) + " MXN\n\n"
                  "Estimad@ " + cliente + ", Happy Burger agradece tu preferencia\n\n¡Hasta Pronto :D!\n")
            ticketW.close()

            """Se lee el archivo .txt para mostrar el ticket"""
            ticketR = open("ticket.txt", "r")
            datos = ticketR.read()
            print(datos)
            ticketR.close()
            print("------------------------------")

            """ En caso de generar un error por parte de la conexión y/o en la inserción de los datos entra la excepción al error """
        except sqlite3.Error as e:
            print("Error al intentar insertar el pedido: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminarPedido(self):
        """ Elimina por completo los datos de un pedido que ya han sido guardados:
        Se maneja un bloque se sentencias y excepciones para conectarse a la base de datos y seleccionar el contenido """
        try:
            conexion = self.baseDatos.abrirConexion()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Pedidos")
            pedidos = cursor.fetchall()

            """ Código condicional para asegurar que existan pedidos en la base de datos """
            if len(pedidos) > 0:
                print("Lista de pedidos para eliminar: ")

                """se muestran los pedidos actualmente guardados"""
                self.mostrarPedidos()
                print("--------------------------------")

                """se pide al usuario que introduzca el ID del pedido que desea modificar"""
                id_pedido = self.ingresarID("Ingresa el ID del pedido a eliminar \n")

                """Se selecciona el pedido con el ID que ingresó el usuario"""
                encontrar_pedido = cursor.execute("SELECT * FROM Pedidos WHERE id = ?", (id_pedido,))

                """Condicional para asegurar que el pedido se encuentre en la base de datos"""
                if len(encontrar_pedido.fetchall()) == 1:

                    """Se borran los datos del pedido en la base de datos y se guarda el cambio"""
                    sql = '''DELETE FROM Pedidos WHERE id = ?'''
                    cursor.execute(sql, (id_pedido,))
                    conexion.commit()
                    print("Pedido eliminado correctamente")
                    print("--------------------------------")

                    """En caso de no haber registros con ese ID, se envía un mensaje con esa información"""
                else:
                    print("No hay pedidos con ese ID")
                    print("--------------------------------")

                """En caso de no haber pedidos en la base de datos se envía un mensaje con esa información"""
            else:
                print("No hay pedidos para eliminar")
                print("--------------------------------")

            """Excepción al error en la eliminación del registro"""
        except sqlite3.Error as e:
            print("Error al intentar eliminar el pedido: {}".format(e))

            """ Se ejecuta el código sin importar la excepción: cerrar la conexión a la base de datos """
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def ingresarID(self,mensaje):
        """Función para ingresar el ID de un registro existente en la base de datos y eliminarlo o buscarlo"""
        id_pedido = 0
        datos_incorrectos = True

        """Bucle y bloque de sentencias con excepciones para pedir que el usuario introduzca el ID del pedido"""
        while datos_incorrectos:

            """Entrada del input y terminación del bucle while"""
            try:
                id_pedido = int(input( mensaje ))
                datos_incorrectos = False

                """Excepción en caso de haber error al capturar el ID del cliente y continuación del bucle while"""
            except Exception as e:
                print("Error al capturar el ID del pedido: {}".format(e))
                print("Intente de nuevo ingresar el ID \n")
                datos_incorrectos = True

            """Retorna el id del pedido"""
        return id_pedido

    def ingresarDatosPedido(self):
        """Función para ingresar los datos del pedido y realizar algún registro nuevo"""
        datos_incorrectos = True

        """Bucle y bloque de excepciones para ingresar los datos solicitados por la base de datos"""
        while datos_incorrectos:
            try:
                pedido = int(input("Ingresa el número de pedido: \n"))
                cliente = input("Ingresa el nombre del cliente: \n")
                producto = input("Ingresa el nombre del producto: \n")
                precio = float(input("Ingresa el precio del producto: \n"))

                """Se termina el bucle while"""
                datos_incorrectos = False

                """Excepcion en caso de haber un error al capturar un dato"""
            except Exception as e:
                print("Error al capturar un dato: {}".format(e))
                print("Intente de nuevo ingresar los datos \n")
                datos_incorrectos = True

            """Retorna los datos escritos por el usuario"""
        return pedido,cliente,producto,precio