import customtkinter as ctk
from tkinter import filedialog

from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico

class Tela():
    def __init__(self):
        #interface grafica
        self.app = ctk.CTk()

        self.app.title("Analisador Léxico")
        self.app.geometry("1280x650")
        self.app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        #area para escrever
        self.label = ctk.CTkLabel(self.app, text="Código:")
        self.label.grid(row=0, column=0, padx=10)
        self.textBox = ctk.CTkTextbox(self.app)
        self.textBox.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew", padx=(10, 10), pady=10)

        #area para mostrar analise lexica
        self.textBoxResult = ctk.CTkTextbox(self.app, state="disabled")
        self.textBoxResult.grid(row=0, column=4, rowspan=2, sticky="nsew", padx=(0, 10), pady=(10, 0))

        #area para mostrar analise sintatica
        self.textBoxSintatico = ctk.CTkTextbox(self.app, state="disabled")
        self.textBoxSintatico.grid(row=2, column=4, rowspan=2, sticky="nsew", padx=(0, 10), pady=10)

        #botao d analisar
        self.btnAnalisar = ctk.CTkButton(self.app, text="Analisar", command=self.__analisar)
        self.btnAnalisar.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        #botao para importar arquivo
        self.btnImportar = ctk.CTkButton(self.app, text="Importar Arquivo", command=self.__importar_arquivo)
        self.btnImportar.grid(row=4, column=3, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.app.mainloop()
        
    def __importar_arquivo(self):
        #pega o caminho do arquivo
        arquivo = filedialog.askopenfile(mode='r', initialdir='./Desktop', title='Selecione um arquivo', filetypes=([('Arquivos de Texto', '*.txt')]))
        
        #abre o arquivo
        conteudo = arquivo.read()
        
        #coloca o texto no textBox
        self.textBox.delete('1.0', 'end')
        self.textBox.insert('end', conteudo)
        
    def __analisar(self):
        analisadorLexico = AnalisadorLexico()
        analisadorSintatico = AnalisadorSintatico()
        
        tokens = analisadorLexico.analisar(self.textBox, self.textBoxResult)
        analisadorSintatico.analisar(entrada=tokens, text_box=self.textBoxSintatico)
        
if __name__ == '__main__':
    tela = Tela()