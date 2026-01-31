import cargarDatos as cd

alumnos = cd.getdatos()
asignaturas = cd.getasignaturas()


def validarAsignatura(
    asignatura: str,
):  # Valida si la asignatura ingresada esta en el diccionario
    if asignatura.capitalize().strip() in asignaturas:
        return True
    else:
        return False


def nuevAsignatura():
    print("**************************************")
    print("********* AGREGAR ASIGNATURA *********")
    print("**************************************")
    asign = input("Ingrese el Nombre de la Nueva Asignatura: ").capitalize().strip()
    if (
        asign == "" or asign.isdigit()
    ):  # valida que la asignatura no sea un campo vacio o un numero
        return print("Ingrese un Nombre Valido para la Nueva Asignatura")

    elif validarAsignatura(asign):  # valida que la asignatura no este registrada
        print("La Asignatura ya se Encuentra Registrada")
    else:
        asignaturas.append(asign)  # Agrega la asignatura a la lista
        cd.setasignaturas(asignaturas)  # guarda la nueva asignatura en archivo json
        cd.getasignaturas()  # Actualiza la lista de asignaturas
        print("Nueva Asignatura Registrada")


def listarAsignaturas():
    print("******************************************")
    print("********* LISTADO DE ASIGNATURAS *********")
    print("******************************************")
    ordenada = sorted(asignaturas)  # crea una lista ordenada de asignaturas
    for asignatura in ordenada:  # imprime cada asignatura
        print(f"{asignatura}")


def eliminarAsignatura():
    print("***************************************")
    print("********* ELIMINAR ASIGNATURA *********")
    print("***************************************")
    asignatura = input("Ingrese el nombre de la asignatura: ").capitalize().strip()
    if (
        asignatura in asignaturas
    ):  # consulta si la asignatura ingresada por teclado esta en asignaturas
        asignaturas.remove(asignatura)  # si se encuentra la elimina
        cd.setasignaturas(asignaturas)  # Guarda los nuevos cambios
        cd.getasignaturas()  # Actualiza las asignaturas
        print("Asignatura Eliminada")
    else:
        print("La Asignatura no se encuentra registrada")
