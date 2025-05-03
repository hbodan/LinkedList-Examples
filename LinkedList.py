"""
Nombre: Harry Enrique Bodán Navarro
Versión del programa: 1.0
Fecha de realización: 02 de Mayo 2025
Resumen:
Este programa implementa una lista enlazada que permite insertar nodos de forma ordenada, eliminar nodos con un valor específico 
y recorrer la lista para imprimirla. Los nodos contienen una clave y un puntero al siguiente nodo.
"""

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, node):
        if self.head == None:
            self.head = node
        else:
            if node.key <= self.head.key:
                node.next = self.head
                self.head = node
            else:
                current = self.head
                while current.next is not None and current.next.key < node.key:
                     current = current.next
                node.next = current.next
                current.next = node
    
    def removeNode(self, valor):
        while self.head and self.head.key == valor:
            self.head = self.head.next

        current = self.head
        while current and current.next:
            if current.next.key == valor:
                current.next = current.next.next
            elif current.next.key > valor:
                break
            else:
                current = current.next
                    
    def printList(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next
                
class Node:
    def __init__(self, dato):
        self.key = dato
        self.next = None
        
    def __str__(self):
       return f"Clave -> {self.key}"
        