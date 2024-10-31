from collections import defaultdict

class Grafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.grafo = defaultdict(list)

    def ler_arquivo(self, arquivo):
        # Lê o arquivo e preenche a lista de adjacências
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas[1:]:  # Ignora a primeira linha com o número de vértices
                linha = linha.strip()
                if linha and ',' in linha:  # Verifica se a linha não está vazia e contém uma vírgula
                    v1, v2 = linha.split(',')
                    self.grafo[v1].append(v2)
                    self.grafo[v2].append(v1)  # Grafo não direcionado

    def exibir_lista_adjacencia(self):
        # Exibe a lista de adjacência para cada vértice
        print("Lista de Adjacências:")
        for vertice, vizinhos in self.grafo.items():
            print(f"{vertice}: {vizinhos}")

def main():
    # Questão 1: Representação do Grafo a partir da Lista de Adjacências
    print("Representação do GRAFO1.txt")
    grafo1 = Grafo()
    grafo1.ler_arquivo("GRAFO1.txt")
    grafo1.exibir_lista_adjacencia()

    print("\nRepresentação do GRAFO2.txt")
    grafo2 = Grafo()
    grafo2.ler_arquivo("GRAFO2.txt")
    grafo2.exibir_lista_adjacencia()

if __name__ == "__main__":
    main()
