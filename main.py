from LinkedList import *
from Exercise1 import *
from Exercise2 import *
from Exercise3 import *
from Exercise4 import *

def main():
    while True:
        print("\nHiii!")
        print("¿Qué ejercicio deseas ejecutar?")
        print("1. Ejercicio 1: Estudiantes ordenados")
        print("2. Ejercicio 2: Mapa con estaciones de ruta")
        print("3. Ejercicio 3: Gestión de pacientes en la clínica")
        print("4. Ejercicio 4: Historial de acciones en el editor de texto")
        print("5. Salir")

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            exercise1()
        elif choice == '2':
            exercise2()
        elif choice == '3':
            exercise3()
        elif choice == '4':
            exercise4()
        elif choice == '5':
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
main()