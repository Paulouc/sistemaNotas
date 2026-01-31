import cargarDatos as cd  # se importa el archivo cargarDatos con las conexiones a los archivos json

alumnos = cd.getdatos()  # extrae los datos de los alumnos
asignaturas = cd.getasignaturas()  # extrae los datos de las asignaturas


# Metodo para validar que solo acepte espacios y letras
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


def listarAlumnos():  # metodo que lista los nombres de los alumnos
    for nombre in alumnos:
        print(nombre)


def agregarAlumno():  # metodo para agregar alumnos
    print("**********************************")
    print("********* AGREGAR ALUMNO *********")
    print("**********************************")
    nombre = input("Ingrese el nombre del alumno: ").capitalize().strip()
    if ValidarNombreAlumno(
        nombre
    ):  # se toma el nombre ingresado por teclado y se valida que solo sean espacios o letras
        if (
            nombre not in alumnos
        ):  # si el nombre no esta en alumnos se agrega en la linea de abajo
            alumnos[nombre.capitalize().strip()] = {}
            cd.setdatos(alumnos)  # se cargan los datos a json
            print("Alumno Agregado")
            cd.getdatos()  # se actualizan los datos de alumnos
            print(nombre)
        else:  # si el nombre esta en la lista imprime error
            print("El alumno ya se encuentra registrado")


def eliminarAlumno():
    print("***********************************")
    print("********* ELIMINAR ALUMNO *********")
    print("***********************************")
    nombre = input("Ingrese el nombre del alumno: ")
    if (
        nombre.capitalize().strip() in alumnos
    ):  # se toma el nombre agregado por teclado y se busca en el diccionario alumnos
        alumnos.pop(
            nombre.capitalize().strip()
        )  # si se encuentra una coincidencia esta se elimina
        cd.setdatos(alumnos)  # se cargan los datos a json
        print("Alumno Eliminado")
        cd.getdatos()  # se actualiza el diccionario alumnos
    else:
        print("El alumno no se encuentra registrado")
