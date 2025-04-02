class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        sum_digits = sum(int(digit) for digit in str(key))
        return sum_digits % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)
    
    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]


class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()
    
    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
        print()
    
    def shortest_path(self, start, end):
        queue = [(start, [start])]
        visited = set()
        
        while queue:
            node, path = queue.pop(0)
            if node == end:
                print("Shortest path:", ' -> '.join(map(str, path)))
                return
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        print("No path found")


if __name__ == "__main__":
    # Hash Table Example
    ht = HashTable()
    ht.insert(123456)
    print("Search 123456:", "Found" if ht.search(123456) else "Not Found")
    
    # Graph Example
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    
    print("BFS Traversal:", end=' ')
    g.bfs(0)
    
    print("DFS Traversal:", end=' ')
    g.dfs(0)
    
    print("Finding Shortest Path (0 -> 4):")
    g.shortest_path(0, 4)
