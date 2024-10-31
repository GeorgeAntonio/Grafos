from collections import defaultdict

class Grafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.grafo_lista = defaultdict(list)
        self.grafo_matriz = []
        self.matriz_incidencia = []
        self.vertices = set()  # Conjunto para armazenar os vértices únicos
        self.arestas = []      # Lista de arestas para a matriz de incidência

    def ler_arquivo(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacências
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas[1:]:  # Ignora a primeira linha com o número de vértices
                linha = linha.strip()
                if linha and ',' in linha:  # Verifica se a linha não está vazia e contém uma vírgula
                    v1, v2 = linha.split(',')
                    self.grafo_lista[v1].append(v2)
                    self.grafo_lista[v2].append(v1)  # Grafo não direcionado
                    self.vertices.update([v1, v2])
                    self.arestas.append((v1, v2))  # Armazena as arestas

    def construir_matriz_adjacencia(self):
        # Constrói a matriz de adjacência usando os vértices do grafo
        n = len(self.vertices)
        vertices_ordenados = sorted(self.vertices)
        indice = {v: i for i, v in enumerate(vertices_ordenados)}  # Mapeia cada vértice a um índice
        self.grafo_matriz = [[0] * n for _ in range(n)]

        for v1, vizinhos in self.grafo_lista.items():
            for v2 in vizinhos:
                i, j = indice[v1], indice[v2]
                self.grafo_matriz[i][j] = 1
                self.grafo_matriz[j][i] = 1  # Grafo não direcionado

    def construir_matriz_incidencia(self):
        # Constrói a matriz de incidência usando vértices e arestas
        n = len(self.vertices)
        m = len(self.arestas)
        vertices_ordenados = sorted(self.vertices)
        indice = {v: i for i, v in enumerate(vertices_ordenados)}  # Mapeia cada vértice a um índice
        self.matriz_incidencia = [[0] * m for _ in range(n)]

        for k, (v1, v2) in enumerate(self.arestas):
            i, j = indice[v1], indice[v2]
            self.matriz_incidencia[i][k] = 1
            self.matriz_incidencia[j][k] = 1  # Aresta conecta dois vértices

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência para cada vértice
        print("Lista de Adjacências:")
        for vertice, vizinhos in self.grafo_lista.items():
            print(f"{vertice}: {vizinhos}")

    def exibir_matriz_adjacencia(self):
        # Exibe a matriz de adjacência
        print("Matriz de Adjacências:")
        for linha in self.grafo_matriz:
            print(" ".join(map(str, linha)))

    def exibir_matriz_incidencia(self):
        # Exibe a matriz de incidência
        print("Matriz de Incidência:")
        for linha in self.matriz_incidencia:
            print(" ".join(map(str, linha)))

def main():
    # Questão 1: Representação do Grafo a partir da Lista de Adjacências
    print("Representação do GRAFO1.txt - Lista de Adjacências")
    grafo1 = Grafo()
    grafo1.ler_arquivo("GRAFO1.txt")
    grafo1.exibir_lista_adjacencia()
    
    # Questão 2: Representação do Grafo a partir da Matriz de Adjacências
    grafo1.construir_matriz_adjacencia()
    print("\nRepresentação do GRAFO1.txt - Matriz de Adjacências")
    grafo1.exibir_matriz_adjacencia()

    # Questão 3: Representação do Grafo a partir da Matriz de Incidência
    grafo1.construir_matriz_incidencia()
    print("\nRepresentação do GRAFO1.txt - Matriz de Incidência")
    grafo1.exibir_matriz_incidencia()

    print("\n" + "="*30 + "\n")

    # Repetir para o GRAFO2.txt
    print("Representação do GRAFO2.txt - Lista de Adjacências")
    grafo2 = Grafo()
    grafo2.ler_arquivo("GRAFO2.txt")
    grafo2.exibir_lista_adjacencia()
    
    # Questão 2: Matriz de Adjacências para GRAFO2.txt
    grafo2.construir_matriz_adjacencia()
    print("\nRepresentação do GRAFO2.txt - Matriz de Adjacências")
    grafo2.exibir_matriz_adjacencia()

    # Questão 3: Matriz de Incidência para GRAFO2.txt
    grafo2.construir_matriz_incidencia()
    print("\nRepresentação do GRAFO2.txt - Matriz de Incidência")
    grafo2.exibir_matriz_incidencia()

if __name__ == "__main__":
    main()
