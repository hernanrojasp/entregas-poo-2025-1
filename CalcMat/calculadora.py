class Matriz2x2:
    

    def __init__(self, datos):
        
        if len(datos) != 2 or any(len(fila) != 2 for fila in datos):
            raise ValueError("Se requiere una matriz de 2 filas por 2 columnas.")
        self.datos = datos

    def sumar(self, otra):
        return Matriz2x2([
            [self.datos[i][j] + otra.datos[i][j] for j in range(2)]
            for i in range(2)
        ])

    def restar(self, otra):
        return Matriz2x2([
            [self.datos[i][j] - otra.datos[i][j] for j in range(2)]
            for i in range(2)
        ])

    def multiplicar(self, otra):
        a = self.datos
        b = otra.datos
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return Matriz2x2(c)

    def mostrar(self):
        for fila in self.datos:
            print(f"| {fila[0]}  {fila[1]} |")

def pedir_matriz(nombre):
    """
    Pide al usuario los valores de una matriz 2x2.
    """
    print(f"\n--- Ingreso de {nombre} ---")
    contenido = []
    for fila in range(2):
        datos_fila = []
        for columna in range(2):
            while True:
                try:
                    val = int(input(f"Ingrese el valor de {nombre}[{fila}][{columna}]: "))
                    datos_fila.append(val)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
        contenido.append(datos_fila)
    return Matriz2x2(contenido)

def ejecutar_calculadora():
    """
    Ejecuta el programa de operaciones con matrices.
    """
    print("=== Operaciones con Matrices 2x2 ===")
    mat_a = pedir_matriz("Matriz A")
    mat_b = pedir_matriz("Matriz B")

    print("\n--- Matriz A ---")
    mat_a.mostrar()
    print("\n--- Matriz B ---")
    mat_b.mostrar()

    print("\nSeleccione una operación:")
    print("  1 - Suma")
    print("  2 - Resta")
    print("  3 - Multiplicación")

    opcion = input("Opción: ")

    if opcion == "1":
        resultado = mat_a.sumar(mat_b)
        print("\n> Resultado de la suma:")
    elif opcion == "2":
        resultado = mat_a.restar(mat_b)
        print("\n> Resultado de la resta:")
    elif opcion == "3":
        resultado = mat_a.multiplicar(mat_b)
        print("\n> Resultado de la multiplicación:")
    else:
        print("Opción inválida.")
        return

    resultado.mostrar()

if __name__ == "__main__":
    ejecutar_calculadora()
