from collections import defaultdict

class Digrafo:
    def __init__(self):
        # Usando um dicionário para representar a lista de adjacência
        self.digrafo = defaultdict(list)

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
                
                print(f"O arquivo {arquivo} foi lido com sucesso.")
                
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

def main():
    # Representação do Digrafo a partir da Lista de Arestas
    print("\nRepresentação do DIGRAFO1.txt")
    digrafo1 = Digrafo()
    digrafo1.ler_lista_arestas("DIGRAFO1.txt")
    digrafo1.exibir_lista_adjacencia()

    print("\nRepresentação do DIGRAFO2.txt")
    digrafo2 = Digrafo()
    digrafo2.ler_lista_arestas("DIGRAFO2.txt")
    digrafo2.exibir_lista_adjacencia()

if __name__ == "__main__":
    main()
