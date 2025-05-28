from datetime import datetime

def obtener_pregunta(numero):
    preguntas = [
        "¿Cuántas mascotas va a ingresar?",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Perro (Kaiser)?",
        "¿Qué edad tiene 'Kaiser'?",
        "¿De qué raza es 'Kaiser'?",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Peluza)?",
        "¿Qué edad tiene 'Peluza'?",
        "¿De qué raza es 'Peluza'?",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Tiger)?",
        "¿Qué edad tiene 'Tiger'?",
        "¿De qué raza es 'Tiger'?"
    ]
    return preguntas[numero] if numero < len(preguntas) else "No hay más preguntas."

def obtener_respuesta(pregunta):
    respuestas = {
        "¿Cuántas mascotas va a ingresar?": "3",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?": "Perro",
        "¿Cuál es el nombre del Perro (Kaiser)?": "Kaiser",
        "¿Qué edad tiene 'Kaiser'?": "9",
        "¿De qué raza es 'Kaiser'?": "Lobo",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Peluza)?": "Peluza",
        "¿Qué edad tiene 'Peluza'?": "8",
        "¿De qué raza es 'Peluza'?": "Siames",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Tiger)?": "Tiger",
        "¿Qué edad tiene 'Tiger'?": "5",
        "¿De qué raza es 'Tiger'?": "Angora"
    }
    return respuestas.get(pregunta, "")

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def obtener_info(self):
        return [self.__class__.__name__, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def registrar_mascotas():
    mascotas = [
        Perro("Kaiser", 9, "Lobo"),
        Gato("Peluza", 8, "Siames"),
        Gato("Tiger", 5, "Angora")
    ]
    return mascotas

def mostrar_mascotas(mascotas):
    print("\nResumen de mascotas registradas:")
    print("|Clase |Nombre   |Edad    |Raza         |Fecha de ingreso         |")
    print("|------|---------|--------|-------------|--------------------------|")
    for mascota in mascotas:
        clase, nombre, edad, raza, fecha = mascota.obtener_info()
        print(f"|{clase:<6}|{nombre:<9}|{edad:<8}|{raza:<13}|{fecha:<26}|")

# Corrección: __main__ estaba mal escrito como "_main_"
if __name__ == "__main__":
    numero_pregunta = 0
    while True:
        pregunta = obtener_pregunta(numero_pregunta)
        print(f"> {pregunta}")
        respuesta = obtener_respuesta(pregunta)
        if respuesta:
            print(f"< {respuesta}")
        numero_pregunta += 1
        if pregunta == "No hay más preguntas.":
            break

    mascotas = registrar_mascotas()
    mostrar_mascotas(mascotas)
