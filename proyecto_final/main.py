from administracion_clientes import AdministracionListaClientes
from administracion_menu import AdministracionMenu
from administracion_pedidos import AdministracionPedido
#Saúl Pulido
#27/09/2023
#Proyecto final: Avance 1

"""Módulo para iniciar la aplicación"""
class Menu:
    def __init__(self):
        self.iniciarMenu()

    def iniciarMenu(self):
        """Se relaciona un objeto con la clase creada para su funcionalidad"""
        listaClientes = AdministracionListaClientes()
        print("-----------------")
        print("Sistema de Happy Burger :D")
        salir_programa = False

        """Se inicializa un bucle para entrar en el programa y comenzar la navegación entre las interfaces"""
        while not salir_programa:
            print("Interfaz Principal: Seleccione una opción presionando el número correspondiente")
            print("""
                1.- Pedidos
                2.- Clientes
                3.- Menú
                4.- Salir del sistema
                """)
            
            """Se le pide al usuario que escriba el número de acuerdo a la opción que desea elegir en la interfaz mostrada"""
            opcion = int(input("Escribe el número de la opción deseada y presiona Enter"))

            """En caso de elegir la opción 1, se mostrará la base de datos actual de los pedidos, así como la interfaz de selección para crear o eliminar un pedido"""
            if opcion == 1:
                listaPedidos = AdministracionPedido()
                listaPedidos.mostrarPedidos()
                salir_pedidos = False

                """Se inicializa un bucle para navegar a través de la interfaz de selección"""
                while not salir_pedidos:
                    print("Listado de pedidos")
                    print("""
                        1.- Crear pedido
                        2.- Cancelar pedido
                        3.- Regresar al menú anterior
                        """)
                    
                    """Se le pide al usuario ingresar el número correspondiente a la opción deseada de la interfaz mostrada"""
                    opcion = int(input("Escribe el número de la opción deseada y presiona Enter"))

                    """Al seleccionar 1 comienza el método agregarPedido()"""
                    if opcion == 1:
                        listaPedidos.agregarPedido()

                        """Al seleccionar 2 comienza el método eliminarPedido()"""
                    elif opcion == 2:
                        listaPedidos.eliminarPedido()

                        """Al seleccionar 3 regrea al menú anterior"""
                    if opcion == 3:
                        print("Regresando al menú anterior")

                        """Sale del bucle de la interfaz de pedidos"""
                        salir_pedidos = True

                    """Continua en la selección de las opciones en la interfaz principal"""
                continue

                """En caso de elegir la opción 2 se mostrará la base de datos de los clientes, así como la interfaz de selección para añadir un cliente, modificar su información o eliminar uno"""
            elif opcion == 2:
                listaClientes.mostrarListaClientes()
                salir_clientes = False

                """Se inicializa un bucle para navegar a través de la interfaz de selección"""
                while not salir_clientes:
                    print("Listado de clientes")
                    print("""
                        1.- Agregar cliente
                        2.- Elimnar cliente
                        3.- Actualizar cliente
                        4.- Regresar al menú anterior
                        """)
                    
                    """Se le pide al usuario ingresar el número correspondiente a la opción deseada de la interfaz mostrada"""
                    opcion = int(input("Escribe el número de la opción deseada y presiona Enter"))

                    """Al seleccionar 1 comienza el método agregarCliente()"""
                    if opcion == 1:
                        listaClientes.agregarCliente()

                        """Al seleccionar 2 comienza el método eliminarCliente()"""
                    elif opcion == 2:
                        listaClientes.eliminarClientes()

                        """Al seleccionar 3 comienza el método modificarCliente()"""
                    elif opcion == 3:
                        listaClientes.modificarCliente()

                        """Al seleccionar 4 regrea al menú anterior"""
                    if opcion == 4:
                        print("Regresando al menú anterior")

                        """Sale del bucle de la interfaz de los clientes"""
                        salir_clientes = True

                    """Continua en la selección de las opciones en la interfaz principal"""
                continue

                """En caso de elegir la opción 3 se mostrará la base de datos de los productos, así como la interfaz de selección para añadir un producto, modificar su información o eliminar uno"""
            elif opcion == 3:
                listaProductos = AdministracionMenu()
                listaProductos.mostrarMenu()
                salir_menu = False

                """Se inicializa un bucle para navegar a través de la interfaz de selección"""
                while not salir_menu:
                    print("Menú de Happy Burger")
                    print("""
                        1.- Agregar producto
                        2.- Elimnar producto
                        3.- Actualizar producto
                        4.- Regresar al menú anterior
                        """)
                    
                    """Se le pide al usuario ingresar el número correspondiente a la opción deseada de la interfaz mostrada"""
                    opcion = int(input("Escribe el número de la opción deseada y presiona Enter"))

                    """Al seleccionar 1 comienza el método agregarProducto()"""
                    if opcion == 1:
                        listaProductos.agregarProducto()

                        """Al seleccionar 2 comienza el método eliminarProductos()"""
                    elif opcion == 2:
                        listaProductos.eliminarProductos()

                        """Al seleccionar 3 comienza el método modificarProducto()"""
                    elif opcion == 3:
                        listaProductos.modificarProducto()

                        """Al seleccionar 4 regresa al menú anterior"""
                    if opcion == 4:
                        print("Regresando al menú anterior")

                        """Sale del bucle de la interfaz de los productos"""
                        salir_menu = True

                    """Continua en la selección de las opciones en la interfaz principal"""
                continue

                """En caso de elegir la opción 4 sale del programa"""
            if opcion == 4:
                print("Estás saliendo del programa, ¡hasta pronto!")

                """Se termina el bucle de la interfaz principal"""
                salir_programa = True

"""Se manda llamar el aplicativo"""
sistema_HappyBurger = Menu()