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
        "¿Cuál es el nombre del Gato (Felix)?",
        "¿Qué edad tiene 'Felix'?",
        "¿De qué raza es 'Felix'?"
    ]
    return preguntas[numero] if numero < len(preguntas) else "No hay más preguntas."

def obtener_respuesta(pregunta):
    respuestas = {
        "¿Cuántas mascotas va a ingresar?": "3",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?": "Perro",
        "¿Cuál es el nombre del Perro?": "Kaiser",
        "¿Qué edad tiene 'Kaiser'?": "9",
        "¿De qué raza es 'Kaiser'?": "Lobo",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Peluza)?": "Peluza",
        "¿Qué edad tiene 'Peluza'?": "8",
        "¿De qué raza es 'Peluza'?": "Siames",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Felix)?": "Felix",
        "¿Qué edad tiene 'Felix'?": "5",
        "¿De qué raza es 'Felix'?": "Angora"
    }
    return respuestas.get(pregunta, "")

class Mascota:
    def _init_(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().strftime("2025-04-20T18:25:55")

    def obtener_info(self):
        return [self._class.name_, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def registrar_mascotas():
    mascotas = [
        Perro("Kaiser", 9, "Lobo",),
        Gato("Peluza", 8, "Siames"),
        Gato("Felix", 5, "Angora")
    ]
    return mascotas

def mostrar_mascotas(mascotas):
    print("Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    print("|------|---------|-------|-------------|--------------------------|")
    for mascota in mascotas:
        print(f"|{mascota.obtener_info()[0]:<6}|{mascota.obtener_info()[1]:<9}|{mascota.obtener_info()[2]:<7}|{mascota.obtener_info()[3]:<13}|{mascota.obtener_info()[4]:<26}|")

if __name__ == "_main_":
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
    print()
    mascotas = registrar_mascotas()
    mostrar_mascotas(mascotas)
    