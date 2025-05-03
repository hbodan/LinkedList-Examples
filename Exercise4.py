"""
Nombre: Harry Enrique Bodán Navarro
Versión del programa: 1.0
Fecha de realización: 02 de Mayo 2025
Resumen: 
Este programa tiene como objetivo implementar un historial de acciones realizadas por un usuario en un editor de texto. 
Las acciones como escribir, borrar, pegar y copiar deben ser almacenadas en orden y deben permitir la navegación en ambas direcciones. 
El sistema debe simular las acciones de Deshacer (Undo) y Rehacer (Redo) para permitir que el usuario revierta o repita acciones previas durante su interacción con el editor.
"""

from LinkedList import *

class Action:
    def __init__(self, action_type, content):
        self.action_type = action_type
        self.content = content
        
    def __str__(self):
        return f"Action: {self.action_type}, Content: {self.content}"

class HistoryManager:
    def __init__(self):
        self.history = LinkedList()
        self.current = None
        
    def add_action(self, action):
        node = Node(action)
        self.appendNode(node)
        self.current = node 
    
    def appendNode(self, node):
        if self.history.head is None:
            self.history.head = node
            self.current = node
        else:
            current = self.history.head
            while current.next:
                current = current.next
            current.next = node

    def undo(self):
        if self.current and self.current != self.history.head:
            current = self.history.head
            while current.next != self.current:
                current = current.next
            self.current = current
            print(f"Deshacer: {self.current.key}")
        else:
            print("No hay más acciones para deshacer.")
    
    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Rehacer: {self.current.key}")
        else:
            print("No hay más acciones para rehacer.")

    def print_history(self):
        print("Historial de acciones:")
        self.history.printList()
        

def exercise4():
    action1 = Action("write", "Hello")
    action2 = Action("delete", "o")
    action3 = Action("paste", "World")

    history_manager = HistoryManager()

    history_manager.add_action(action1)
    history_manager.add_action(action2)
    history_manager.add_action(action3)

    history_manager.print_history()

    print("\nRealizando Deshacer:")
    history_manager.undo()

    print("\nRealizando Deshacer nuevamente:")
    history_manager.undo()

    print("\nRealizando Rehacer:")
    history_manager.redo()

    print("\nRealizando Rehacer nuevamente:")
    history_manager.redo()