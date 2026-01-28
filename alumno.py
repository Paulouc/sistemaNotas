import cargarDatos as cd

alumnos = cd.getdatos()
asignaturas = cd.getasignaturas()


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


def listarAlumnos():
    for nombre in alumnos:
        print(nombre)


def validarAsignatura(asignatura: str):
    if asignatura.lower() in asignaturas:
        return True
    else:
        return False


def nuevAsignatura(asignatura: str):
    if asignatura == "" or asignatura.isdigit():
        return print("Ingrese un Nombre Valido para la Nueva Asignatura")

    elif validarAsignatura(asignatura):
        print("La Asignatura ya se Encuentra Registrada")
    else:
        asignaturas.append(asignatura)
        cd.setasignaturas(asignaturas)
        cd.getasignaturas()
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
    nombre = input("Ingrese el nombre del alumno: ")
    if ValidarNombreAlumno(nombre):
        if nombre not in alumnos:
            alumnos[nombre] = {}
            # alumnos = {nombre: {"": []}}
            cd.setdatos(alumnos)
            print("Alumno Agregado")
            cd.getdatos()
            print(cd.getdatos())

        else:
            print("El alumno ya se encuentra registrado")


def AgregarNotas(nombreAlumno):
    print("********* AGREGAR NOTAS *********")
    while True:
        if nombreAlumno in alumnos:
            asign = input(
                f"asignaturas: {asignaturas} \nIngrese el nombre de la asignatura: "
            ).strip()
            print(asign)
            if validarAsignatura(asign):
                if "" in alumnos[nombreAlumno]:
                    alumnos[nombreAlumno].pop("")
                    alumnos[nombreAlumno][asign] = []

                elif asign not in alumnos[nombreAlumno]:
                    alumnos[nombreAlumno][asign] = []

                cd.setdatos(alumnos)
                cd.getdatos()
                print(alumnos)
                nota = input("Ingrese la nota: ")
                if validaNota(nota):  # retorna True si la asignatura esta registrada
                    # agrega una nota a la lista dentro de alumnos[nombreAlumno][asign][nota]
                    alumnos[nombreAlumno][asign].append(nota)
                    cd.setdatos(alumnos)
                    cd.getdatos()
                    print(alumnos)
                    ####  Agregar codigo para guardar lista dentro de documento json
                    opcion = input(
                        "nota agregada correctamente, desea agregar otra? S/N... "
                    ).lower()
                    if opcion == "s":
                        continue
                    else:
                        break
                else:
                    print("Ingrese una nota valida")
        else:
            print("El alumno no existe")
            break
