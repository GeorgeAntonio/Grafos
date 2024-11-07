from collections import defaultdict

class Digrafo:
    def __init__(self):
        # Inicializa as estruturas necessárias
        self.digrafo = defaultdict(list)
        self.tempo = 0
        self.entrada = {}
        self.saida = {}
        self.vertices = set()
        self.arestas = []
        self.matriz_adjacencia = []
        self.matriz_incidencia = []
        self.n_vertices = 0
        self.n_arestas = 0

    def ler_lista_arestas(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacência e matriz de adjacência
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()
                
                if not linhas:
                    print(f"O arquivo {arquivo} está vazio.")
                    return
                
                # Lê a primeira linha para obter o número de vértices
                self.n_vertices = int(linhas[0].strip())
                # Inicializa a matriz de adjacência com zeros
                self.matriz_adjacencia = [[0] * self.n_vertices for _ in range(self.n_vertices)]
                self.arestas = []  # Limpa a lista de arestas para preencher a partir do arquivo

                # Preenche a lista de adjacência e a matriz de adjacência
                for linha in linhas[1:]:
                    linha = linha.strip()
                    if linha and ',' in linha:
                        v1, v2 = map(int, linha.split(','))
                        self.digrafo[str(v1)].append(str(v2))
                        self.matriz_adjacencia[v1 - 1][v2 - 1] = 1
                        self.vertices.update([str(v1), str(v2)])
                        self.arestas.append((v1, v2))  # Armazena a aresta como tupla (v1, v2)
                
                print(f"\nMatriz de Adjacência para {arquivo}:")
                for linha in self.matriz_adjacencia:
                    print(" ".join(map(str, linha)))
                
                # Após preencher as arestas, gera a matriz de incidência
                self.gerar_matriz_incidencia()

        except FileNotFoundError:
            print(f"O arquivo {arquivo} não foi encontrado.")
        except ValueError:
            print(f"O arquivo {arquivo} contém dados inválidos.")

    def gerar_matriz_incidencia(self):
        # Gera a matriz de incidência a partir das arestas
        self.n_arestas = len(self.arestas)
        self.matriz_incidencia = [[0] * self.n_arestas for _ in range(self.n_vertices)]

        for j, (v1, v2) in enumerate(self.arestas):
            # Ajusta índices para a matriz (vértices começam em 1 no arquivo)
            self.matriz_incidencia[v1 - 1][j] = -1  # Origem da aresta
            self.matriz_incidencia[v2 - 1][j] = 1   # Destino da aresta

        print("\nMatriz de Incidência:")
        for linha in self.matriz_incidencia:
            print(" ".join(map(str, linha)))

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência para cada vértice
        print("Lista de Adjacências:")
        if not self.digrafo:
            print("O digrafo está vazio ou não foi carregado corretamente.")
        else:
            for vertice, vizinhos in self.digrafo.items():
                print(f"{vertice}: {vizinhos}")

    def dfs(self, vertice, visitado):
        # Realiza a busca em profundidade, registrando os tempos de entrada e saída
        visitado.add(vertice)
        self.entrada[vertice] = self.tempo
        print(f"Entrou no vértice {vertice} no tempo {self.tempo}")
        self.tempo += 1

        for vizinho in self.digrafo[vertice]:
            if vizinho not in visitado:
                self.dfs(vizinho, visitado)

        self.saida[vertice] = self.tempo
        print(f"Saiu do vértice {vertice} no tempo {self.tempo}")
        self.tempo += 1

    def busca_profundidade(self):
        # Inicializa a DFS e percorre todos os vértices para garantir a visita de todos os componentes
        visitado = set()
        self.tempo = 0
        self.entrada = {}
        self.saida = {}

        vertices = list(self.digrafo.keys())
        for vertice in vertices:
            if vertice not in visitado:
                self.dfs(vertice, visitado)

        print("\nTempos de Entrada e Saída:")
        for vertice in vertices:
            print(f"Vértice {vertice}: Entrada = {self.entrada.get(vertice, 'N/A')}, Saída = {self.saida.get(vertice, 'N/A')}")

def main():
    # Representação do Digrafo a partir da Lista de Arestas
    print("\nRepresentação do DIGRAFO1.txt a partir da Lista de Arestas")
    digrafo1 = Digrafo()
    digrafo1.ler_lista_arestas("DIGRAFO1.txt")
    #digrafo1.exibir_lista_adjacencia()

    print("\nRepresentação do DIGRAFO2.txt a partir da Lista de Arestas")
    digrafo2 = Digrafo()
    digrafo2.ler_lista_arestas("DIGRAFO2.txt")
    #digrafo2.exibir_lista_adjacencia()

    # Busca em profundidade e exibição dos tempos de entrada e saída
    print("\nBusca em Profundidade para o DIGRAFO1.txt")
    digrafo1.busca_profundidade()

    print("\nBusca em Profundidade para o DIGRAFO2.txt")
    digrafo2.busca_profundidade()

if __name__ == "__main__":
    main()
