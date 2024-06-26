class Simbolo: 
    def __init__(self, nome, categoria, tipo, nivel):
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.nivel = nivel
        
class TabelaDeSimbolos:
    def __init__(self):
        self.escopos = [{}]
        
    def entrar_escopo(self):
        self.escopos.append({})
        
    def sair_escopo(self):
        if len(self.escopos) > 1:
            self.escopos.pop()
        
    def inserir(self, simbolo):
        escopo_atual = self.escopos[-1]
        escopo_atual[simbolo.nome] = simbolo
        
        self.imprimir_tabela()
        
    def buscar(self, nome):
        for escopo in reversed(self.escopos):  # Procura do escopo mais interno para o mais externo
            if nome in escopo:
                return escopo[nome]
        return None  # Se não encontrado em nenhum escopo
    
    def imprimir_tabela(self):
        tabela = "Nome | Categoria | Tipo | Nível\n"
        tabela += "-" * 30 + "\n"
        for escopo in self.escopos:
            for simbolo in escopo.values():
                tabela += f"{simbolo.nome} | {simbolo.categoria} | {simbolo.tipo} | {simbolo.nivel}\n"
        print(tabela)
            
    # def remover(self, simbolo):
    #     self.simbolos.pop(simbolo)
    
    # def __str__(self):
    #     tabela = "Nome | Categoria | Tipo | Nível\n"
    #     tabela += "-" * 30 + "\n"
    #     for simbolo in self.simbolos:
    #         tabela += f"{simbolo.nome} | {simbolo.categoria} | {simbolo.tipo} | {simbolo.nivel}\n"
    #     return tabela