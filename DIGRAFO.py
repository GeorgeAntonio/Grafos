from collections import defaultdict

class Digrafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.digrafo = defaultdict(list)
        self.tempo = 0
        self.entrada = {}
        self.saida = {}

    def ler_lista_arestas(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacências para um digrafo a partir de uma lista de arestas
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()
                
                if not linhas:
                    print(f"O arquivo {arquivo} está vazio.")
                    return
                
                # Ignora a primeira linha, que contém o número de vértices
                for linha in linhas[1:]:
                    linha = linha.strip()
                    if linha and ',' in linha:  # Verifica se a linha não está vazia e contém uma vírgula
                        v1, v2 = linha.split(',')
                        self.digrafo[v1].append(v2)  # Adiciona a aresta direcionada de v1 para v2
                
                print(f"O arquivo {arquivo} foi lido com sucesso (Lista de Arestas).")
                
        except FileNotFoundError:
            print(f"O arquivo {arquivo} não foi encontrado.")
        except ValueError:
            print(f"O arquivo {arquivo} contém dados inválidos.")

    def ler_matriz_incidencia(self, arquivo):
        # Lê o arquivo e exibe a matriz de incidência para um digrafo
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()
                
                if not linhas:
                    print(f"O arquivo {arquivo} está vazio.")
                    return
                
                # Exibir a matriz de incidência lida do arquivo
                print(f"\nMatriz de Incidência para {arquivo}:")
                n = int(linhas[0].strip())  # Primeira linha indica o número de vértices
                matriz_incidencia = []
                
                for j in range(1, len(linhas[1:]) + 1):
                    linha = [int(x) for x in linhas[j].strip().split()]
                    matriz_incidencia.append(linha)
                    print(" ".join(map(str, linha)))  # Imprimir cada linha da matriz

                    # Conversão para lista de adjacência
                    origem = -1
                    destino = -1
                    for i, valor in enumerate(linha):
                        if valor == -1:
                            origem = str(i)
                        elif valor == 1:
                            destino = str(i)
                    
                    if origem != -1 and destino != -1:
                        self.digrafo[origem].append(destino)  # Aresta direcionada de origem para destino
                
                print(f"O arquivo {arquivo} foi lido e convertido com sucesso para lista de adjacência (Matriz de Incidência).")
                
        except FileNotFoundError:
            print(f"O arquivo {arquivo} não foi encontrado.")
        except ValueError:
            print(f"O arquivo {arquivo} contém dados inválidos.")

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência para cada vértice
        print("Lista de Adjacências:")
        if not self.digrafo:
            print("O digrafo está vazio ou não foi carregado corretamente.")
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

        # Criar uma lista estática dos vértices para evitar modificação durante a iteração
        vertices = list(self.digrafo.keys())
        for vertice in vertices:
            if vertice not in visitado:
                self.dfs(vertice, visitado)

        # Exibindo tempos de entrada e saída
        print("\nTempos de Entrada e Saída:")
        for vertice in vertices:
            print(f"Vértice {vertice}: Entrada = {self.entrada[vertice]}, Saída = {self.saida[vertice]}")

def main():
    # Representação do Digrafo a partir da Lista de Arestas
    print("\nRepresentação do DIGRAFO2.txt a partir da Lista de Arestas")
    digrafo2 = Digrafo()
    digrafo2.ler_lista_arestas("DIGRAFO2.txt")
    digrafo2.exibir_lista_adjacencia()

    print("\nRepresentação do DIGRAFO3.txt a partir da Lista de Arestas")
    digrafo3 = Digrafo()
    digrafo3.ler_lista_arestas("DIGRAFO3.txt")
    digrafo3.exibir_lista_adjacencia()

    # Representação do Digrafo a partir da Matriz de Incidência
    print("\nRepresentação do DIGRAFO2.txt a partir da Matriz de Incidência")
    digrafo2_matriz = Digrafo()
    digrafo2_matriz.ler_matriz_incidencia("DIGRAFO2.txt")
    digrafo2_matriz.exibir_lista_adjacencia()

    print("\nRepresentação do DIGRAFO3.txt a partir da Matriz de Incidência")
    digrafo3_matriz = Digrafo()
    digrafo3_matriz.ler_matriz_incidencia("DIGRAFO3.txt")
    digrafo3_matriz.exibir_lista_adjacencia()

    # Executar a busca em profundidade e exibir tempos de entrada e saída
    print("\nBusca em Profundidade para o DIGRAFO2.txt")
    digrafo2.busca_profundidade()

    print("\nBusca em Profundidade para o DIGRAFO3.txt")
    digrafo3.busca_profundidade()

if __name__ == "__main__":
    main()
