import cargarDatos as cd  # se importa el archivo cargarDatos con las conexiones a los archivos json
from asignatura import validarAsignatura  # se carga metodo para validar asignatura

alumnos = cd.getdatos()
asignaturas = cd.getasignaturas()


def validaNota(cadena):  # validar que el numero que se ingresa sea un float
    try:
        # Reemplazamos coma por punto para que Python lo entienda como decimal
        float(cadena.replace(",", "."))
        if 1.0 <= float(cadena) <= 7.0:  # validamos que la nota sea entre 1.0 y 7.0
            return True
        else:  # devuelve error si no se cumplen las condiciones
            print("La nota debe estar entre 1.0 y 7.0")
            return False
    except ValueError:
        return False


def eliminarNota():
    print("*********************************")
    print("********* ELIMINAR NOTA *********")
    print("*********************************")
    nombreAlumno = input("Ingrese el nombre del alumno: ").capitalize().strip()
    if (
        nombreAlumno in alumnos
    ):  # si el nombre ingresado por teclado coincide con alguno en alumnos
        print(alumnos[nombreAlumno])
        asignatura = (
            input("Ingrese el nombre de la asignatura: ").capitalize().strip()
        )  # solicita asignatura
        if (
            asignatura in alumnos[nombreAlumno]
        ):  # Y valida que el alumno esta cursando la asignatura
            print(
                f"Ha seleccionado al Estudiante {nombreAlumno} y la asignatura {asignatura}"
            )
            nota = input(
                f"Que nota desea eliminar?.... {alumnos[nombreAlumno][asignatura]}"  # solicita la nota a eliminar y muestras las notas correspondientes al alumno y asignatura ingresados anteriormente
            ).strip()
            if validaNota(
                nota
            ):  # valida que la nota sea float y que este entre 1.0 y 7.0
                if (
                    nota in alumnos[nombreAlumno][asignatura]
                ):  # si la nota ingresada coincide con la que esta ingresada al diccionario
                    alumnos[nombreAlumno][asignatura].remove(nota)  # se elimina la nota
                    cd.setdatos(alumnos)  # se cargan los datos a json
                    cd.getdatos()  # se actualizan los datos de alumnos
                    print("Nota Eliminada")
                    print(
                        alumnos[nombreAlumno][asignatura]
                    )  # Imprime las notas segun alumno y asignatura


def AgregarNotas():
    print("*********************************")
    print("********* AGREGAR NOTAS *********")
    print("*********************************")
    alumnosin = list(alumnos.keys())  # Crea una lista con los nombres de los alumnos
    nombreAlumno = (
        input(
            f"Alumnos: {alumnosin} \nIngrese el nombre del alumno: "
        )  # Muestra los alumnos ingresados y solicita ingresar el nombre del alumno al que ingresara la nota
        .capitalize()
        .strip()
    )
    while True:
        if (
            nombreAlumno in alumnosin
        ):  # si el nombre ingresado por teclado esta en la lista creada con los nombres de alumnos
            asign = (
                input(
                    f"asignaturas: {asignaturas} \nIngrese el nombre de la asignatura: "  # Muestra la lista de asignaturas y solicita ingresar por teclado a que asignatura desea agregar nota
                )
                .capitalize()  # primera letra mayuscula
                .strip()
            )
            if validarAsignatura(
                asign
            ):  # valida si la asignatura ingresada esta en el diccionario
                if (
                    "" in alumnos[nombreAlumno]
                ):  # si encuentra una asignatura en blanco la elimina e ingresa la nueva asignatura
                    alumnos[nombreAlumno].pop("")
                    alumnos[nombreAlumno][asign] = []

                elif (
                    asign not in alumnos[nombreAlumno]
                ):  # de no haber asignaturas en blanco asigna la nueva asignatura
                    alumnos[nombreAlumno][asign] = []

                cd.setdatos(alumnos)  # se guardan los datos
                cd.getdatos()  # se actualiza el diccionario
                nota = input("Ingrese la nota: ")
                if validaNota(nota):  # valida si la nota es un numero entre 1.0 y 7.0
                    alumnos[nombreAlumno][asign].append(
                        nota
                    )  # agrega una nota a la lista dentro de alumnos[nombreAlumno][asign][nota]
                    cd.setdatos(alumnos)  # se guardan datos en json
                    cd.getdatos()  # se actualizan los datos de alumnos
                    print(f"{nombreAlumno} = {asign}: {alumnos[nombreAlumno][asign]}")
                    opcion = input(
                        "nota agregada correctamente, desea agregar otra? S/N...  "  # consulta si quiere agregar una nueva nota para el mismo alumno y asignatura
                    ).lower()
                    if (
                        opcion == "s"
                    ):  # si la respuesta es "s" (si) se repite el proceso
                        continue
                    else:  # si se responde n o cualquier otra letra, vuelve al menu anterior
                        break
                else:
                    print("Ingrese una nota valida")
        else:
            print("El alumno no existe")
            break


# función para calcular el promedio de un alumno
def obtenerPromedio(datos_alumno):
    notas = []  # creamos un diccionario de notas
    for (
        materia
    ) in (
        datos_alumno.values()
    ):  # Por cada materia en los valores del diccionario de alumnos
        notas.extend(
            [float(n) for n in materia]
        )  # Convertimos cada nota de string a float
    return sum(notas) / len(notas) if notas else 0  # calcula el proimedio o entrega 0


def rankingNotas():
    print("*********************************")
    print("*********** RANKINIG ************")
    print("*********************************")

    alumnos_ordenados = dict(  # diccionario para guardar la lista ordenada
        sorted(
            alumnos.items(),  # Convierte el diccionario en una lista de parejas (Nombre, datos).
            key=lambda item: obtenerPromedio(
                item[
                    1
                ]  # ingresa el elemento con el indice [1] y se ejecuta para cada elemento del iterable
            ),  # indica que el parametro para ordenar los items es el promedio
            reverse=True,  # para que invierta el orden y asi queden de mayor a menor
        )
    )
    # se listan nombre y promedio de cada alumno en el diccionario alumnos_ordenados
    for nombre, datos in alumnos_ordenados.items():
        print(f"{nombre}: Promedio {obtenerPromedio(datos):.2f}")


def listarNotas():
    print("*********************************")
    print("********** LISTA NOTAS  *********")
    print("*********************************")
    for (
        nombre,
        datos,
    ) in (
        alumnos.items()
    ):  # itera e imprime nombre del alumno, asignatura, notas y promedio de cada asignatura
        print(f"Nombre: {nombre}\nAsignaturas: \n{datos}):")
        print(f"Promedio {obtenerPromedio(datos):.2f}")
