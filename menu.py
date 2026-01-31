import alumno as al, asignatura as asg, notas as nt  # importa alumnos, asignaturas y notas


def menu():
    while True:  # menu bucle infinito, solo se detiene al pinchar la opcion salir
        print("*************************************")  # opciones del menu principal
        print(
            "********* SISTEMA DE NOTAS **********"
        )  # Cada opcion tiene un modulo propio
        print("*************************************")
        print("1. Alumnos")
        print("2. Notas")
        print("3. Asignaturas")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                while True:
                    print("**********************************")
                    print(
                        "********** MENU ALUMNOS **********"
                    )  # Opciones del menu Alumnos
                    print("**********************************")
                    print("1. Agregar Alumnos")
                    print("2. Listar Alumnos")
                    print("3. Eliminar Alumnos")
                    print("4. Volver al menu principal")
                    opcionAlumno = input("Ingrese una opcion: ")
                    match opcionAlumno:
                        case "1":
                            al.agregarAlumno()  # llama a metodo de la clase alumno
                        case "2":
                            al.listarAlumnos()
                        case "3":
                            al.eliminarAlumno()
                        case "4":
                            break
                        case _:
                            print("Opcion invalida")
            case "2":
                while True:
                    print("**********************************")
                    print(
                        "*********** MENU NOTAS ***********"
                    )  # Opciones del menu Notas
                    print("**********************************")
                    print("1. Agregar Notas")
                    print("2. Ver Notas")
                    print("3. Eliminar nota")
                    print("4. Ranking")
                    print("5. Volver al menu principal")
                    opcioNota = input("Ingrese una opcion: ")
                    match opcioNota:
                        case "1":
                            nt.AgregarNotas()  # llama a metodo de la clase notas
                        case "2":
                            nt.listarNotas()
                        case "3":
                            nt.eliminarNota()
                        case "4":
                            nt.rankingNotas()  # Ranking de los promedios de mayor a menor
                        case "5":
                            break
            case "3":
                while True:
                    print("**********************************")
                    print(
                        "******** MENU ASIGNATURAS ********"
                    )  # Opciones del menu Asignaturas
                    print("**********************************")
                    print("1. Agregar Asignatura")
                    print("2. Listar Asignaturas")
                    print("3. Eliminar Asignatura")
                    print("4. Volver al menu principal")
                    opcionAsign = input("Ingrese una opcion: ")
                    match opcionAsign:
                        case "1":
                            asg.nuevAsignatura()  # llama a metodo de la clase asignaturas
                        case "2":
                            asg.listarAsignaturas()
                        case "3":
                            asg.eliminarAsignatura()
                        case "4":
                            break
            case "4":
                break


menu()
