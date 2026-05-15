# 6. Analizador de notas

# Pide 5 notas y al final muestra:

# promedio
# nota mayor
# nota menor
# cuántos aprobaron

# Supón que aprobar es >= 70.

# Temas:

# listas
# acumuladores
# max/min
# lógica


notas = []
resultado = 0
promedio = 0


def pedirCargarNota(cantidad):
    while cantidad < 5:
        nota = int(input("Ingrese la nota del estudiante: "))
        notas.append(nota)
        print("Nota agregada correctamente")
    print("Notas agregadas:")
    print(notas)


pedirCargarNota()
