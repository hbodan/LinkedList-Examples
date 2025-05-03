"""
Nombre: Harry Enrique Bodán Navarro
Versión del programa: 1.0
Fecha de realización: 02 de Mayo 2025
Resumen: 
Este programa tiene como objetivo automatizar un mapa con las estaciones de una ruta previamente establecida. 
El sistema debe ser capaz de calcular y mostrar el tiempo estimado para llegar desde un punto de la ruta hasta cualquier destino en la misma ruta. 
Se debe permitir al usuario indicar su ubicación de inicio y destino, y el programa debe calcular el tiempo basado en el tiempo de viaje entre las estaciones.
"""

from LinkedList import *

class Station:
    def __init__(self, id, name, time_to_previous):
        self.id = id
        self.name = name
        self.time_to_previous = time_to_previous

    def __str__(self):
        return f"{self.id}: {self.name} - Time to previous: {self.time_to_next} min"
    

class RouteMap(LinkedList):
    def insert_node(self, node):
        if self.head is None:
            node.time_to_previous = 0
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_between(self, new_station, before_station_name):
        current = self.head
        while current:
            if current.key.name == before_station_name:
                new_node = Node(new_station)
                if current.next:
                    current.next.key.time_to_previous -= new_node.key.time_to_previous
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    
        print(f"Estación {before_station_name} no fue encontrada.")
        
    def estimated_time(self, origin, destination):
        current = self.head
        time = 0
        in_route = False
        while current:
            if current.key.name == origin:
                in_route = True
            if in_route:
                if current.next: 
                    time += current.next.key.time_to_previous
            if current.key.name == destination:
                break
            current = current.next
        return time if in_route else "Origen de ruta no encontrada"

def exercise2():
    route = RouteMap()

    route.insert_node(Node(Station("T001", "Terminal", 0)))
    route.insert_node(Node(Station("T002", "Alamo", 5)))    
    route.insert_node(Node(Station("T003", "Boreal", 3)))  
    route.insert_node(Node(Station("T004", "Aboli", 7)))  

    print("** Casos Iniciales **")
    # Tiempo entre Terminal y Aboli
    print(f"Tiempo estimado entre Terminal y Aboli: {route.estimated_time('Terminal', 'Aboli')} minutos") 
    
    # Insertar una estación entre Alamo y Boreal
    print("\n** Insertando una nueva estación entre Alamo y Boreal **")
    route.insert_between(Station("T005", "Boreal-Intermedio", 2), "Alamo") 
    
    # Tiempo entre las estaciones después de la inserción
    print(f"Tiempo estimado entre Terminal y Aboli (después de la inserción): {route.estimated_time('Terminal', 'Aboli')} minutos")
    print(f"Tiempo estimado entre Alamo y Boreal-Intermedio: {route.estimated_time('Alamo', 'Boreal-Intermedio')} minutos")
    print(f"Tiempo estimado entre Boreal-Intermedio y Boreal: {route.estimated_time('Boreal-Intermedio', 'Boreal')} minutos")
    
    # Insertar estación entre Boreal y Aboli
    print("\n** Insertando otra estación entre Boreal y Aboli **")
    route.insert_between(Station("T006", "Aboli-Intermedio", 3), "Boreal") 
    
    # Tiempo entre las estaciones después de la segunda inserción
    print(f"Tiempo estimado entre Terminal y Aboli (después de la segunda inserción): {route.estimated_time('Terminal', 'Aboli')} minutos")
    print(f"Tiempo estimado entre Boreal y Aboli-Intermedio: {route.estimated_time('Boreal', 'Aboli-Intermedio')} minutos")
    print(f"Tiempo estimado entre Aboli-Intermedio y Aboli: {route.estimated_time('Aboli-Intermedio', 'Aboli')} minutos")
    
    # Verificar caso en el que se inserta una estación antes de la primera estación
    print("\n** Insertando una estación antes de la primera estación (Terminal) **")
    route.insert_between(Station("T007", "Inicio", 0), "Terminal")

    # Tiempo estimado entre la nueva estación de inicio y la primera estación
    print(f"Tiempo estimado entre Inicio y Terminal: {route.estimated_time('Inicio', 'Terminal')} minutos")
    print(f"Tiempo estimado entre Terminal y Alamo: {route.estimated_time('Terminal', 'Alamo')} minutos")
    
    # Verificar caso en el que la estación no se encuentra
    print("\n** Intentando insertar una estación antes de una estación no existente **")
    route.insert_between(Station("T008", "NoExistente", 5), "Inexistente")
