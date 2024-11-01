from collections import defaultdict

class Digrafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.grafo = defaultdict(list)

    def ler_arquivo(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacências para um grafo não direcionado
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas[1:]:  # Ignora a primeira linha com o número de vértices
                linha = linha.strip()
                if linha and ',' in linha:  # Verifica se a linha não está vazia e contém uma vírgula
                    v1, v2 = linha.split(',')
                    self.grafo[v1].append(v2)
                    self.grafo[v2].append(v1)  # Grafo não direcionado

    def ler_matriz_adjacencia(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacências para um digrafo usando matriz de adjacência
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            n = int(linhas[0].strip())  # Primeira linha indica o número de vértices
            for i in range(1, n + 1):
                linha = linhas[i].strip().split()  # Lê cada linha como uma lista de valores
                for j, valor in enumerate(linha):
                    if valor == '1':  # Verifica se há uma aresta direcionada
                        self.grafo[str(i - 1)].append(str(j))

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência para cada vértice
        print("Lista de Adjacências:")
        for vertice, vizinhos in self.grafo.items():
            print(f"{vertice}: {vizinhos}")

def main():
    # Representação do Digrafo a partir da Matriz de Adjacências
    print("\nRepresentação do DIGRAFO1.txt")
    digrafo1 = Digrafo()
    digrafo1.ler_matriz_adjacencia("DIGRAFO1.txt")
    digrafo1.exibir_lista_adjacencia()

    print("\nRepresentação do DIGRAFO2.txt")
    digrafo2 = Digrafo()
    digrafo2.ler_matriz_adjacencia("DIGRAFO2.txt")
    digrafo2.exibir_lista_adjacencia()

if __name__ == "__main__":
    main()
