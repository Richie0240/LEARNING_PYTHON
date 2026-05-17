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


def cargar_notas(cantidad):

    contador = 0

    while contador < cantidad:

        try:
            nota = int(input(f"Ingrese la nota del estudiante #{contador + 1}: "))

        except ValueError:
            print("Debe ingresar un número válido\n")
            continue

        notas.append(nota)

        print("Nota agregada correctamente\n")

        contador += 1

    return notas


def calcularPromedio(notas):
    suma = 0
    for i in notas:
        suma += i
    promedio = suma / len(notas)
    return promedio


def encontrarMenor(notas):
    notaMenor = min(notas)
    notaMayor = max(notas)
    return notaMenor, notaMayor


def aprobaron(notas):
    estudiantesAprobados = 0
    for i in notas:
        if i >= 70:
            estudiantesAprobados += 1

    reprobados = len(notas) - estudiantesAprobados

    return estudiantesAprobados, reprobados


cargar_notas(5)

notaMenor, notaMayor = encontrarMenor(notas)
estudiantesAprobados, reprobados = aprobaron(notas)
print("El promedio de las notas es: ", calcularPromedio(notas))
print("La nota mas baja es: ", notaMenor, " y la nota mayor es: ", notaMayor)
print(
    "La cantidad de estudiantes aprobados: ",
    estudiantesAprobados,
    " y la cantidad de estudiantes reprobados: ",
    reprobados,
)
