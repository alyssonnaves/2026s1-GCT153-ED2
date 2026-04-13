class Grafo:

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = []
        for _ in range(self.num_vertices):
            self.adj.append([])
        
    def adicionar_aresta(self, origem: int, destino: int) -> None:
        if destino not in self.adj[origem]:
            self.adj[origem].append(destino)
            self.adj[destino].append(origem)

    def exibir(self):
        for vertice in range(self.num_vertices):
            print(f"{vertice}: {self.adj[vertice]}")

    def grau(self, vertice: int) -> int:
        return len(self.adj[vertice]) # devolve o tamanho da lista adjacente

    def eh_vizinho(self, vertice_a: int, vertice_b: int):
        for v in self.adj[vertice_a]:
            if vertice_b ==  v:
                return True
        return False
        
if __name__ == "__main__":
    g = Grafo(10)
    print(g.adj)
    g.adicionar_aresta(3,1)    
    g.adicionar_aresta(3,2)
    g.adicionar_aresta(1,2)
    g.adicionar_aresta(1,9)
    g.adicionar_aresta(5,7)
    g.adicionar_aresta(7,6)
    g.adicionar_aresta(4,2)
    g.adicionar_aresta(1,9)
    print(g.adj)
    g.exibir()
    print(f"Grau: {g.grau(2)}")
    print("vizinhos")
    print(g.eh_vizinho(1,9))