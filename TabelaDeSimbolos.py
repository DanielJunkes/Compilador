class Simbolo: 
    def __init__(self, nome, categoria, tipo, nivel):
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.nivel = nivel
        
class TabelaDeSimbolos: 
    def __init__(self):
        self.escopos = [{}] # lista de dicionários que representam escopos
        
    def entrarEscopo(self):
        self.escopos.append({}) # cria um novo escopo vazio e o adiciona a lista de escopos
        
    def sairEscopo(self):
        if len(self.escopos) > 1:
            self.escopos.pop() # remove o escopo mais interno da lista de escopos
        
    def inserir(self, simbolo, text_box):
        escopo_atual = self.escopos[-1]
        escopo_atual[simbolo.nome] = simbolo # adiciona um símbolo ao escopo mais interno
        
        self.imprimirTabela(text_box)
        
    def buscar(self, nome):
        for escopo in reversed(self.escopos):  # procura do escopo mais interno para o mais externo
            if nome in escopo:
                return escopo[nome]
        return None  
    
    def buscarNoEscopo(self, nome):
        escopo_atual = self.escopos[-1]
        return escopo_atual.get(nome, None)
    
    def imprimirTabela(self, text_box):
        tabela = "Nome | Categoria | Tipo | Nível\n"
        tabela += "-" * 30 + "\n"
        for escopo in self.escopos:
            for simbolo in escopo.values():
                tabela += f"{simbolo.nome} | {simbolo.categoria} | {simbolo.tipo} | {simbolo.nivel}\n"
        text_box.configure(state="normal")
        text_box.insert("end", f"{tabela}\n")
        text_box.configure(state="disabled")