import json


def setdatos(datos: dict):
    try:
        with open(
            "archivos/datos.json", "w", encoding="utf-8"
        ) as archivo:  # abre el archivo (datos.json) con metodo de escritura
            json.dump(
                datos, archivo, ensure_ascii=False, indent=4
            )  # copia los datos del parametro al archivo
    except Exception as e:
        print("error al exportar los datos", e)


def getdatos():
    try:
        with open(
            "archivos/datos.json", "r", encoding="utf-8"
        ) as archivo:  # abre el archivo (datos.json) con metodo de lectura
            datos = json.load(
                archivo
            )  # carga los datos del archivo datos.json al diccionario dato
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío/corrupto, devuelve una lista vacía
        return {}  # o devuelve un diccionario vacio


# lo mismo que los metodos de arriba pero guarda y devuelve una lista
def setasignaturas(datos: list):
    try:
        with open("archivos/asignaturas.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print("error al exportar los datos", e)


def getasignaturas():
    try:
        with open("archivos/asignaturas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío/corrupto, devuelve una lista vacía
        return []
