# Crud estudiantes


listaEstudiantes = []


def agregarEstudiante():
    nombreEstudiante = input("\nIngrese el nombre del estudiante que desea agregar: ")
    listaEstudiantes.append(nombreEstudiante)
    print("\nEstudiante: ", nombreEstudiante, " agregado correctamente\n")


def verEstudiante():
    for i, estudiante in enumerate(listaEstudiantes):
        print("Estudiante #", i + 1, estudiante, "\n")


def eliminarEstudiante():
    verEstudiante()
    eliminado = int(input("\nIngrese el numero del estudiante que desea borrar: "))
    if eliminado < 1 or eliminado > len(listaEstudiantes):
        print("Ese estudiante no se encuentra en la lista")
        return
    print(
        "\nEstudiante: ",
        listaEstudiantes[eliminado - 1],
        ", eliminado satisfactoriamente \n",
    )
    listaEstudiantes.pop(eliminado - 1)


def editarEstudiante():
    verEstudiante()

    try:
        aEditar = int(input("\nIngrese el numero del estudiante que desea editar: "))
    except:
        print("Ingrese un numero valido")
        return

    if aEditar < 1 or aEditar > len(listaEstudiantes):
        print("Ese estudiante no se encuentra en la lista")
        return

    nombre = input(
        "Ingrese el nombre corregido para el estudiante #" + str(aEditar) + " : "
    )

    print(
        "Estudiante #",
        aEditar,
        "editado correctamente",
        "\nnombre anterior: ",
        listaEstudiantes[aEditar - 1],
        "\nnombre actual: ",
        nombre,
    )

    listaEstudiantes[aEditar - 1] = nombre


def menu():
    opcion = ""
    while opcion != "5":
        print("CRUD DE ESTUDIANTES")

        opcion = input(
            "1. Agregar estudiante"
            + "\n"
            + "2. Ver estudiantes"
            + "\n"
            + "3. Eliminar estudiante"
            + "\n"
            + "4. Editar estudiante"
            + "\n"
            + "5. Salir"
            + "\n"
            + "Elija una opcion: "
        )

        if opcion == "1":
            agregarEstudiante()
        elif opcion == "2":
            verEstudiante()
        elif opcion == "3":
            if len(listaEstudiantes) >= 1:
                eliminarEstudiante()
            else:
                print("No hay estudiantes registrados aun")
        elif opcion == "4":
            if len(listaEstudiantes) >= 1:
                editarEstudiante()
            else:
                print("No hay estudiantes registrados aun")
        elif opcion == "5":
            print("Vuelva pronto")
        else:
            print("opcion incorrecta \n")


menu()
