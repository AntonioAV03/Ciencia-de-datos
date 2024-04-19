# Función para generar una lista de números pseudoaleatorios
def generar_lista_numeros(cantidad_digitos):
    numeros = []  # Inicializamos una lista vacía para almacenar los números
    # Definimos los parámetros para el generador lineal congruente
    a = 1664525
    c = 1013904223
    m = 2**32
    semilla = 1  # Semilla inicial
    for _ in range(cantidad_digitos):  # Iteramos la cantidad de veces especificada
        semilla = (a * semilla + c) % m  # Fórmula del generador lineal congruente
        numero = semilla % 10  # Obtenemos el último dígito del número generado
        numeros.append(numero)  # Agregamos el número generado a la lista
    return numeros  # Retornamos la lista de números pseudoaleatorios

# Función principal del programa
def main():
    try:
        cantidad_digitos = int(input("Ingrese la cantidad de dígitos aleatorios que desea generar: "))  # Solicitamos la cantidad de dígitos

        if cantidad_digitos <= 0:  # Verificamos que la cantidad de dígitos sea positiva
            print("La cantidad de dígitos debe ser un número positivo.")
            return  # Salimos de la función si la cantidad de dígitos es inválida

        lista_numeros = generar_lista_numeros(cantidad_digitos)  # Generamos la lista de números pseudoaleatorios
        print(f"Lista de números pseudoaleatorios de {cantidad_digitos} dígitos:")  # Mostramos un mensaje con la cantidad de dígitos
        print(lista_numeros)  # Mostramos la lista de números pseudoaleatorios en la pantalla
        
    except ValueError:  # Capturamos el error si el usuario ingresa algo que no es un número
        print("Por favor, ingrese un número válido.")

# Verificamos si este archivo se está ejecutando como el programa principal
if __name__ == "__main__":
    main()  # Llamamos a la función main para iniciar el programa
