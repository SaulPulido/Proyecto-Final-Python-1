"""Módulo para realizar la autenticación del personal que ingresa al programa con usuario y contraseña"""
class Autenticacion:
    def verificarAutenticacion(self):
        """Se verifica el ingreso al programa con un bucle while solicitando usuario y contraseña especificos"""
        isLogin = False
        while not isLogin:
            usuario = input("Ingresar usuario: ")
            password = input("Ingresar contraseña: ")

            """Codigo condicional comparando las respuestas del usuario con las correctas"""
            if usuario != 'admin' or password != '1234':
                print("Error de Login")

                """Terminación del bucle"""
            else:
                isLogin = True