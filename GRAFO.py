from collections import defaultdict, deque
from itertools import combinations

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

    def verificar_todas_adjacencias(self):
        # Verifica a adjacência entre todos os pares de vértices
        print("\nVerificação de Adjacência entre Todos os Vértices:")
        for v1, v2 in combinations(self.vertices, 2):
            if v2 in self.grafo_lista[v1]:
                print(f"Vértices '{v1}' e '{v2}' são adjacentes.")
            else:
                print(f"Vértices '{v1}' e '{v2}' não são adjacentes.")

    def total_vertices(self):
        # Retorna o número total de vértices no grafo
        return len(self.vertices)

    def total_arestas(self):
        # Retorna o número total de arestas no grafo
        return len(self.arestas)

    def incluir_vertice(self, vertice):
        # Adiciona um novo vértice ao grafo, sem conexões
        if vertice not in self.vertices:
            self.vertices.add(vertice)
            self.grafo_lista[vertice] = []
            print(f"Vértice '{vertice}' incluído com sucesso.")
            self.exibir_lista_adjacencia()
        else:
            print(f"Vértice '{vertice}' já existe no grafo.")

    def excluir_vertice(self, vertice):
        # Remove um vértice do grafo, incluindo todas as arestas conectadas a ele
        if vertice in self.vertices:
            # Remover o vértice do conjunto de vértices
            self.vertices.remove(vertice)
            
            # Remover o vértice da lista de adjacências de seus vizinhos
            for vizinho in self.grafo_lista[vertice]:
                self.grafo_lista[vizinho].remove(vertice)
            
            # Remover o vértice e suas conexões da lista de adjacências
            del self.grafo_lista[vertice]
            
            # Remover todas as arestas associadas ao vértice
            self.arestas = [(v1, v2) for v1, v2 in self.arestas if v1 != vertice and v2 != vertice]
            
            print(f"Vértice '{vertice}' e todas as suas conexões foram removidos com sucesso.")
            self.exibir_lista_adjacencia()
        else:
            print(f"Vértice '{vertice}' não encontrado no grafo.")

    def eh_conexo(self):
        # Verifica se o grafo é conexo usando DFS
        if not self.vertices:
            return True  # Um grafo vazio é considerado conexo

        visitados = set()
        inicial = next(iter(self.vertices))  # Pega um vértice inicial qualquer
        self._dfs(inicial, visitados)

        if len(visitados) == len(self.vertices):
            print("O grafo é conexo.")
            return True
        else:
            print("O grafo não é conexo.")
            return False

    def _dfs(self, vertice, visitados):
        # Função auxiliar para realizar DFS
        visitados.add(vertice)
        for vizinho in self.grafo_lista[vertice]:
            if vizinho not in visitados:
                self._dfs(vizinho, visitados)

    def eh_bipartido(self):
        # Verifica se o grafo é bipartido usando BFS
        cor = {}
        for vertice in self.vertices:
            if vertice not in cor:  # Se o vértice ainda não foi colorido
                if not self._bfs_bipartido(vertice, cor):
                    print("O grafo não é bipartido.")
                    return False
        print("O grafo é bipartido.")
        return True

    def _bfs_bipartido(self, inicio, cor):
        # Função auxiliar para verificar bipartição usando BFS
        fila = deque([inicio])
        cor[inicio] = 0  # Começamos a colorir o vértice inicial com a cor 0
        while fila:
            vertice = fila.popleft()
            for vizinho in self.grafo_lista[vertice]:
                if vizinho not in cor:
                    # Atribui uma cor oposta ao vértice atual
                    cor[vizinho] = 1 - cor[vertice]
                    fila.append(vizinho)
                elif cor[vizinho] == cor[vertice]:
                    # Se um vizinho tiver a mesma cor, o grafo não é bipartido
                    return False
        return True


    def busca_em_largura(self, vertice_inicial):
        # Realiza a busca em largura a partir de um vértice específico
        visitados = set()
        fila = deque([vertice_inicial])
        resultado = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for vizinho in self.grafo_lista[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)

        print(f"Ordem de visitação na busca em largura a partir de '{vertice_inicial}':", resultado)
        return resultado
    
    def busca_em_profundidade(self, vertice_inicial):
        # Realiza a busca em profundidade a partir de um vértice específico
        visitados = set()
        resultado = []
        self._dfs_exploracao(vertice_inicial, visitados, resultado)
        print(f"Ordem de visitação na busca em profundidade a partir de '{vertice_inicial}':", resultado)
        return resultado

    def _dfs_exploracao(self, vertice, visitados, resultado):
        # Função auxiliar para a DFS explorando o grafo e armazenando o caminho percorrido
        visitados.add(vertice)
        resultado.append(vertice)
        for vizinho in self.grafo_lista[vertice]:
            if vizinho not in visitados:
                self._dfs_exploracao(vizinho, visitados, resultado)

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

    def encontrar_articulacoes_blocos(self):
        discovery_time = {}
        lowpt = {}
        parent = {}
        articulacoes = set()
        biconectados = []
        stack = []
        time = 0

        def dfs(v):
            nonlocal time
            discovery_time[v] = lowpt[v] = time
            time += 1
            children = 0
            is_articulacao = False

            for vizinho in self.grafo_lista[v]:
                if vizinho not in discovery_time:
                    stack.append((v, vizinho))
                    parent[vizinho] = v
                    children += 1
                    dfs(vizinho)
                    
                    lowpt[v] = min(lowpt[v], lowpt[vizinho])
                    
                    if parent.get(v) is None and children > 1:
                        is_articulacao = True
                    elif parent.get(v) is not None and lowpt[vizinho] >= discovery_time[v]:
                        is_articulacao = True
                        componente = []
                        while stack[-1] != (v, vizinho):
                            componente.append(stack.pop())
                        componente.append(stack.pop())
                        biconectados.append(componente)
                        
                elif vizinho != parent.get(v) and discovery_time[vizinho] < discovery_time[v]:
                    lowpt[v] = min(lowpt[v], discovery_time[vizinho])
                    stack.append((v, vizinho))

            if is_articulacao:
                articulacoes.add(v)

        for v in self.vertices:
            if v not in discovery_time:
                dfs(v)
                if stack:
                    biconectados.append(stack[:])
                    stack.clear()

        print("Articulações (Pontos de Corte):", articulacoes)
        print("Blocos (Componentes Biconectados):")
        for i, componente in enumerate(biconectados, 1):
            print(f"Bloco {i}: {componente}")
        return articulacoes, biconectados
    
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

    # Questão 6: Verificação de Adjacência entre Todos os Vértices para GRAFO1
    grafo1.verificar_todas_adjacencias()

    # Questão 7: Número Total de Vértices
    print("\nNúmero Total de Vértices no GRAFO1.txt:", grafo1.total_vertices())

    # Questão 8: Número Total de Arestas
    print("\nNúmero Total de Arestas no GRAFO1.txt:", grafo1.total_arestas())

    # Questão 9: Inclusão de um Novo Vértice
    print("\nInclusão de um novo vértice no GRAFO1.txt")
    novo_vertice = 'z'
    grafo1.incluir_vertice(novo_vertice)

    # Questão 10: Exclusão de um Vértice Existente
    print("\nExclusão de um vértice existente no GRAFO1.txt")
    vertice_para_excluir = 'a'  # Por exemplo, excluindo o vértice 'a'
    grafo1.excluir_vertice(vertice_para_excluir)

    # Questão 11: Verificação de Conectividade para GRAFO1
    print("\nVerificação de Conectividade no GRAFO1.txt")
    grafo1.eh_conexo()

    # Questão 12: Verificação de Bipartição para GRAFO1
    print("\nVerificação se o GRAFO1 é Bipartido")
    grafo1.eh_bipartido()

    # Questão 14: Busca em Largura para GRAFO1
    print("\nBusca em Largura no GRAFO1 a partir de um vértice específico")
    grafo1 = Grafo()
    grafo1.ler_arquivo("GRAFO1.txt")
    vertice_inicial = 'a'  # Defina o vértice inicial para a busca
    grafo1.busca_em_largura(vertice_inicial)

    # Questão 15: Busca em Profundidade para GRAFO1
    print("\nBusca em Profundidade no GRAFO1 a partir de um vértice específico")
    vertice_inicial_grafo1 = 'a'  # Defina o vértice inicial para a busca
    grafo1.busca_em_profundidade(vertice_inicial_grafo1)

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

    # Questão 6: Verificação de Adjacência entre Todos os Vértices para GRAFO2
    grafo2.verificar_todas_adjacencias()

    # Questão 7: Número Total de Vértices
    print("\nNúmero Total de Vértices no GRAFO2.txt:", grafo2.total_vertices())

    # Questão 8: Número Total de Arestas
    print("\nNúmero Total de Arestas no GRAFO2.txt:", grafo2.total_arestas())

    # Questão 11: Verificação de Conectividade para GRAFO2
    print("\nVerificação de Conectividade no GRAFO2.txt")
    grafo2.eh_conexo()

    # Questão 12: Verificação de Bipartição para GRAFO2
    print("\nVerificação se o GRAFO2 é Bipartido")
    grafo2.eh_bipartido()

    print("\n" + "="*30 + "\n")

    # Questão 14: Busca em Largura para GRAFO3
    print("\nBusca em Largura no GRAFO3 a partir de um vértice específico")
    grafo3 = Grafo()
    grafo3.ler_arquivo("GRAFO3.txt")
    vertice_inicial = 'a'  # Defina o vértice inicial para a busca
    grafo3.busca_em_largura(vertice_inicial)

    # Questão 15: Busca em Profundidade para GRAFO3
    print("\nBusca em Profundidade no GRAFO3 a partir de um vértice específico")
    vertice_inicial_grafo3 = 'a'  # Defina o vértice inicial para a busca
    grafo3.busca_em_profundidade(vertice_inicial_grafo3)

    # Questão 16: Determinação de Articulações e Blocos para GRAFO3
    print("\nDeterminação de Articulações e Blocos no GRAFO3.txt")
    grafo3 = Grafo()
    grafo3.ler_arquivo("GRAFO3.txt")
    grafo3.encontrar_articulacoes_blocos()

if __name__ == "__main__":
    main()
