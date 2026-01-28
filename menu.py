import alumno as al
import json


def menu():
    while True:
        print("========S I S T E M A   D E   N O T A S ==========")
        print("1. Alumnos")
        print("2. Notas")
        print("3. Asignaturas")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                while True:
                    print("======== MENU ALUMNOS ==========")
                    print("1. Agregar Alumnos")
                    print("2. Listar Alumnos")
                    print("3. Eliminar Alumnos")
                    print(" . Volver al menu principal")
                    opcionAlumno = input("Ingrese una opcion: ")
                    match opcionAlumno:
                        case "1":
                            al.agregarAlumno()
                            break
                        case "2":
                            al.listarAlumnos()
                        case "3":
                            break
                        case _:
                            print("Opcion invalida")
            case "2":
                while True:
                    print("======== MENU NOTAS ==========")
                    print("1. Agregar Notas")
                    print("2. Ver Notas")
                    print("3. Eliminar nota")
                    # promedio = lambda l: sum(l)/len(l) if len(l) > 0 else 0
                    # notaAlta = lambda l: max(l) if len(l) > 0 else 0
                    # notaBaja = lambda l: min(l) if len(l) > 0 else 0
                    print("3. Volver al menu principal")
                    opcioNota = input("Ingrese una opcion: ")
                    match opcioNota:
                        case "1":
                            nombreAlumno = input("Ingrese el nombre del alumno: ")
                            al.AgregarNotas(nombreAlumno)
                        case "2":
                            print(al.alumnos)
                        case "3":
                            break
            case "3":
                while True:
                    print("======== MENU ASIGNATURAS ==========")
                    print("1. Agregar Asignaturas")
                    print("2. Listar Asignaturas")
                    print("3. Volver al menu principal")
                    opcionAsign = input("Ingrese una opcion: ")
                    match opcionAsign:
                        case "1":
                            asign = input("Ingrese el Nombre de la Nueva Asignatura: ")
                            al.nuevAsignatura(str(asign))
                        case "2":
                            print(al.asignaturas)
                        case "3":
                            break
            case "4":
                break


menu()
