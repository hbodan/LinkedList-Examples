"""
Nombre: Harry Enrique Bodán Navarro
Versión del programa: 1.0
Fecha de realización: 02 de Mayo 2025
Resumen: 
Este sistema está diseñado para gestionar el ingreso de pacientes en una clínica. Los pacientes son ingresados con su nombre, edad, síntoma principal y una prioridad asignada entre 1 y 5. 
El sistema debe permitir insertar nuevos pacientes, mostrar la lista de pacientes ordenada según la prioridad de atención y eliminar pacientes una vez atendidos, 
manejando así un flujo eficiente de atención.
"""

from LinkedList import *

class Patient:
    def __init__(self, name, age, symptom, priority):
        self.name = name
        self.age = age
        self.symptom = symptom
        self.priority = priority 

    def __str__(self):
        return f"Nombre: {self.name}, Edad: {self.age}, Síntomas: {self.symptom}, Prioridad: {self.priority}"

    def __le__(self, other):
        if isinstance(other, Patient):
            return self.priority <= other.priority
        return False
    
    def __lt__(self, other):
        if isinstance(other, Patient):
            return self.priority < other.priority
        return False
    

class PatientWithNameRemove(Patient):
    def __init__(self, name, age, symptom, priority):
        super().__init__(name, age, symptom, priority)
    
    def removeNodeByName(self, patient_list, name):
        current = patient_list.head
        previous = None

        while current is not None:
            if current.key.name == name:
                if previous is None: 
                    patient_list.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        
        return False 

def exercise3():
    patient_list = LinkedList()

    patient1 = PatientWithNameRemove("Andre Joiner", 20, "Dolor de Cabeza", 3)
    patient2 = PatientWithNameRemove("Harry Bodán", 20, "Fiebre Alta", 1)
    patient3 = PatientWithNameRemove("Yorleny Guerrero", 20, "Tos persistente", 2)

    patient_list.insertNode(Node(patient1))
    patient_list.insertNode(Node(patient2))
    patient_list.insertNode(Node(patient3))

    print("Orden de atención:")
    patient_list.printList()

    print("\nElimnando 'Yorleny Guerrero'...")
    patient1.removeNodeByName(patient_list,"Yorleny Guerrero")

    print("\nNuevo Orden:")
    patient_list.printList()