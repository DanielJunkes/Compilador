class Simbolo: 
    def __init__(self, nome, categoria, tipo, nivel):
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.nivel = nivel
        
class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = []
        
    def inserir(self, simbolo):
        self.simbolos.append(simbolo)
        # print('Símbolo inserido:', simbolo.nome, simbolo.tipo)
        tabela = "Nome | Categoria | Tipo | Nível\n"
        tabela += "-" * 30 + "\n"
        for simbolo in self.simbolos:
            tabela += f"{simbolo.nome} | {simbolo.categoria} | {simbolo.tipo} | {simbolo.nivel}\n"
        print(tabela)
        
    def buscar(self, nome):
        for simbolo in self.simbolos:
            if simbolo.nome == nome:
                return simbolo
        return None
    
    def remover(self, simbolo):
        self.simbolos.pop(simbolo)
    
    def __str__(self):
        tabela = "Nome | Categoria | Tipo | Nível\n"
        tabela += "-" * 30 + "\n"
        for simbolo in self.simbolos:
            tabela += f"{simbolo.nome} | {simbolo.categoria} | {simbolo.tipo} | {simbolo.nivel}\n"
        return tabela