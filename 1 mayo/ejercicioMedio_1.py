# 4. Sistema de login simple

# Crea un usuario y contraseña “quemados” en el código.

# El usuario tiene 3 intentos para iniciar sesión.

# Si falla 3 veces:

# Acceso bloqueado

# Si acierta:
# Bienvenido

# Temas:

# while
# if
# contadores
# validación


user = "admin"
pw = "123456"
contador = 0


while contador <= 3:
    userLogin = input("Ingrese el nombre de usuario: ")
    pwLogin = input("Ingrese la contraseña: ")

    if userLogin == user and pwLogin == pw:
        print("Bienvenido")
        break
    else:
        print("Credenciales incorrectas, intente nuevamente")
        contador += 1
    if contador == 3:
        print("Intentos agotados, el sistema se apagara ahora mismo")
        break
