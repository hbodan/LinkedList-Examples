"""
Nombre: Harry Enrique Bodán Navarro
Versión del programa: 1.0
Fecha de realización: 02 de Mayo 2025
Resumen: 
Este programa permite ordenar una lista de estudiantes de un salón de clase según un parámetro indicado por el usuario. 
El parámetro puede ser uno de los siguientes campos: carnet, nombres, apellidos, peso, estatura, sexo o promedio.
El sistema debe mostrar los datos de los estudiantes ordenados de forma ascendente en función del parámetro seleccionado, 
facilitando la organización y visualización de la información.
"""

from LinkedList import *
from functools import total_ordering

class Student:
    def __init__(self, student_id, first_name, last_name, weight, height, gender, average):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight
        self.height = height
        self.gender = gender
        self.average = average

    def __str__(self):
        return (
        f"- ID: {self.student_id} | "
        f"- Name: {self.first_name} {self.last_name} | "
        f"- Weight: {self.weight} | "
        f"- Height: {self.height} | "
        f"- Gender: {self.gender} | "
        f"- Average: {self.average} | "
    )

def order_by(attr):
    @total_ordering
    class OrderedStudent:
        def __init__(self, student):
            self.student = student
            self.criterion = getattr(student, attr)

        def __lt__(self, other):
            return self.criterion < other.criterion

        def __eq__(self, other):
            return self.criterion == other.criterion

        def __str__(self):
            return str(self.student)

    return OrderedStudent

def exercise1():
    attribute = input("¿Por qué campo desea ordenar? (student_id, first_name, last_name, weight, height, gender, average): ").strip()
    StudentKey = order_by(attribute)

    students_list = LinkedList()
    students_list.insertNode(Node(StudentKey(Student("A001", "Harry", "Bodá", 50, 1.42, "M", 85))))
    students_list.insertNode(Node(StudentKey(Student("A002", "Yorleny", "Guerrero", 45, 1.31, "F", 92))))
    students_list.insertNode(Node(StudentKey(Student("A003", "Andre", "Joiner", 60, 1.58, "M", 70))))
    
    print(f"\nEstudiantes ordenados por: {attribute.upper()}\n")
    students_list.printList()