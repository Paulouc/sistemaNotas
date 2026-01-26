alumnos = {}
asignaturas = ["matematicas", "lenguaje", "ciencias"]


def ValidarNombreAlumno(nombre):
    if nombre == "":
        print("Debe ingresar un nombre")
        return False
    elif all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
        # funcion all() toma un iterable y devuelve True si todos sus elementos son Verdaderos, en este caso itera cada letra del nombre ingresado
        # y valida que sea un espacio o una letra
        return True
    else:
        print("No puede ingresar numeros o caracteres especiales.")
        return False


def validarAsignatura(asignatura):
    if asignatura in asignaturas:
        return True
    else:
        return False


def nuevAsignatura(asignatura):
    if asignatura == "" or not str(asignatura).isdigit():
        print("Ingrese un Nombre Valido para la Nueva Asignatura")

    elif validarAsignatura(asignatura):
        print("La Asignatura ya se Encuentra Registrada")
    else:
        asignaturas.append(asignatura)
        print("Nueva Asignatura Registrada")


def validaNota(cadena):
    try:
        # Reemplazamos coma por punto para que Python lo entienda como decimal
        float(cadena.replace(",", "."))
        if 1.0 <= float(cadena) <= 7.0:
            return True
        else:
            print("La nota debe estar entre 1.0 y 7.0")
            return False
    except ValueError:
        return False


def agregarAlumno():
    print("********* AGREGAR ALUMNO *********")
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if ValidarNombreAlumno(nombre):
            alumnos[nombre] = {}
            print(alumnos)
            break


def AgregarNotas(nombreAlumno):
    print("********* AGREGAR NOTAS *********")
    if nombreAlumno not in alumnos:
        alumnos[nombreAlumno] = {}
    while True:
        asign = (
            input(f"asignaturas: {asignaturas} \nIngrese el nombre de la asignatura: ")
            .lower()
            .strip()
        )
        if validarAsignatura(asign):
            if asign not in alumnos[nombreAlumno]:
                alumnos[nombreAlumno][asign] = []
            nota = input("Ingrese la nota: ")
            if validaNota(nota):
                # agrega una nota a la lista dentro de alumnos[nombreAlumno][asign][nota]
                alumnos[nombreAlumno][asign].append(nota)
                opcion = input(
                    "nota agregada correctamente, desea agregar otra? S/N... "
                ).lower()
                if opcion == "s":
                    continue
                else:
                    break
            else:
                print("Ingrese una nota valida")
