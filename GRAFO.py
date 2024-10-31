from collections import defaultdict

class Grafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.grafo_lista = defaultdict(list)
        self.grafo_matriz = []
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

    def calcular_grau(self):
        # Calcula o grau de cada vértice e exibe o resultado
        print("Grau de cada vértice:")
        graus = {vertice: len(vizinhos) for vertice, vizinhos in self.grafo_lista.items()}
        for vertice, grau in graus.items():
            print(f"Vértice {vertice}: Grau {grau}")
        return graus

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

    def matriz_para_lista(self):
        # Converte a matriz de adjacência para a lista de adjacência
        n = len(self.grafo_matriz)
        self.grafo_lista.clear()  # Limpa a lista de adjacência anterior
        for i in range(n):
            for j in range(n):
                if self.grafo_matriz[i][j] == 1:
                    v1 = list(self.vertices)[i]
                    v2 = list(self.vertices)[j]
                    if v2 not in self.grafo_lista[v1]:  # Evita duplicação de arestas
                        self.grafo_lista[v1].append(v2)
                        self.grafo_lista[v2].append(v1)

    def lista_para_matriz(self):
        # Converte a lista de adjacência para a matriz de adjacência
        n = len(self.vertices)
        vertices_ordenados = sorted(self.vertices)
        indice = {v: i for i, v in enumerate(vertices_ordenados)}  # Mapeia cada vértice a um índice
        self.grafo_matriz = [[0] * n for _ in range(n)]

        for v1, vizinhos in self.grafo_lista.items():
            for v2 in vizinhos:
                i, j = indice[v1], indice[v2]
                self.grafo_matriz[i][j] = 1
                self.grafo_matriz[j][i] = 1  # Grafo não direcionado

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

    # Questão 4: Conversão de Matriz de Adjacência para Lista de Adjacência e vice-versa
    print("\nConversão de Matriz de Adjacência para Lista de Adjacência")
    grafo1.matriz_para_lista()
    grafo1.exibir_lista_adjacencia()

    print("\nConversão de Lista de Adjacência para Matriz de Adjacência")
    grafo1.lista_para_matriz()
    grafo1.exibir_matriz_adjacencia()

    # Questão 5: Cálculo do Grau de cada Vértice
    print("\nCálculo do Grau de cada Vértice para GRAFO1.txt")
    grafo1.calcular_grau()

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

    # Questão 4: Conversão de Matriz de Adjacência para Lista de Adjacência e vice-versa para GRAFO2
    print("\nConversão de Matriz de Adjacência para Lista de Adjacência")
    grafo2.matriz_para_lista()
    grafo2.exibir_lista_adjacencia()

    print("\nConversão de Lista de Adjacência para Matriz de Adjacência")
    grafo2.lista_para_matriz()
    grafo2.exibir_matriz_adjacencia()

    # Questão 5: Cálculo do Grau de cada Vértice para GRAFO2
    print("\nCálculo do Grau de cada Vértice para GRAFO2.txt")
    grafo2.calcular_grau()

if __name__ == "__main__":
    main()
