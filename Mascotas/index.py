
import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.datetime.now() 

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}, Fecha de Ingreso: {self.fecha_ingreso}"

class Perro(Mascota):
    def __init__(self, nombre, edad, raza, tamanio):
        super().__init__(nombre, edad, raza)
        self.tamanio = tamanio 

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Tamaño: {self.tamanio}"

class Gato(Mascota):
    def __init__(self, nombre, edad, raza, color):
        super().__init__(nombre, edad, raza)
        self.color = color

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Color: {self.color}"


def ingresar_datos():
    tipo_mascota = input("Ingrese el tipo de mascota (perro/gato): ").lower()
    nombre = input("Ingrese el nombre de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))
    raza = input("Ingrese la raza de la mascota: ")

    if tipo_mascota == "perro":
        tamanio = input("Ingrese el tamaño del perro (pequeño/mediano/grande): ")
        mascota = Perro(nombre, edad, raza, tamanio)
    elif tipo_mascota == "gato":
        color = input("Ingrese el color del gato: ")
        mascota = Gato(nombre, edad, raza, color)
    else:
        print("Tipo de mascota no válido.")
        return None
    
    return mascota

def mostrar_mascotas(mascotas):
    if mascotas:
        for mascota in mascotas:
            print(mascota.mostrar_info())
    else:
        print("No se han ingresado mascotas.")

def main():
    mascotas = []
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar una nueva mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Salir")
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":

            mascota = ingresar_datos()
            if mascota:
                mascotas.append(mascota)
        elif opcion == "2":
            mostrar_mascotas(mascotas)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()

