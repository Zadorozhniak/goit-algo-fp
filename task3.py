import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def dijkstra(self, start):
        # Ініціалізація: відстані до всіх вершин - нескінченність, крім початкової
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        
        # Зберігання вершин та їх поточних відстаней
        priority_queue = [(0, start)]
        
        while priority_queue:
            # Вибір вершини з найменшою відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо поточна відстань більша за збережену, пропускаємо
            if current_distance > distances[current_vertex]:
                continue
                
            # Оновлення відстаней до сусідів
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

# Приклад використання
if __name__ == "__main__":
    g = Graph()
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    
    start_vertex = 'A'
    shortest_paths = g.dijkstra(start_vertex)
    
    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"До {vertex}: {distance}")