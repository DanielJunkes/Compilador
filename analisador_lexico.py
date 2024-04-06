import customtkinter as ctk
from tkinter import filedialog
#dicionario com as palavras reservadas
palavras_reservadas = {'while': 1, 'void': 2, 'string': 3, 'return': 4, 'main': 11, 'literal': 12, 'integer': 13, 'inicio': 14, 'if': 15, 
                       'for': 17, 'float': 18, 'fim': 19, 'else': 20, 'do': 21, 'cout': 22, 'cin': 23, 'char': 24, 
                       'callfuncao': 25}

#dicionario com atribuidores e parentizacao
#nome provisório
atribuidores_parentizacao = {'>': 28, '=': 30, '<': 33, '+': 35, '{': 36, '}': 37, ';': 38, ':': 39, 
                             '/': 40, ',': 41, '*': 42, '(': 43, ')': 44, '$': 45, '-': 48}
atribuidores_duplos = {'>>': 26, '>=': 27, '==': 29, '<=': 31, '<<': 32,'++': 34, '!=': 46, '--': 47}

#dicionario com os tokens dos valores dos dados
valores_dos_dados = {'numerointeiro': 5, 'numerofloat': 6, 'nomevariavel': 7, 'nomedochar': 8, 'nomedastring': 10}

#dicionatio com simbolos que iniciam textos
textos = {'"': 10, "'": 8, '|': 7}

def analisar():
    #lista para salvar os tokens e codigos
    tokens = []
    codigos = []
    linha = []
    
    #variaveis de controle
    comentario_bloco = False
    is_text = False
    
    #limpa o espaço para mostrar o resultado da analise lexica
    textBoxResult.configure(state="normal")
    textBoxResult.delete('1.0', 'end')
    textBoxResult.configure(state="disabled")
    
    #pega o numero de linhas
    linhas = textBox.index('end-1c').split('.')[0]   
    for i in range(1, int(linhas)+1):
        lexema = ''
        #pega o texto que esta na linha
        codigo = textBox.get(f'{i}.0', f'{i}.end')
        
        #percorre o texto da linha
        for j in range(len(codigo)):
            #verifica se tem *\ na linha do para finalizar o comentario em bloco
            if '*\\' in codigo:
                comentario_bloco = False
                break
            if comentario_bloco:
                break
            if codigo[j] == '\\':
                if j+1 < len(codigo):
                    if codigo[j+1] == '\\':
                        break
                    if codigo[j+1] == '*':
                        comentario_bloco = True
                        break
            elif is_text:
                if codigo[j] in textos:
                    is_text = False
                    for key, value in textos.items():
                        if key == codigo[j]:
                            tokens.append(value)
                            codigos.append(lexema)
                            linha.append(i)
                            lexema = ''
                            break
                else:
                    lexema = lexema + codigo[j]
            #verifica se é um dos possiveis atribuidores ou parenteses 
            elif codigo[j] in atribuidores_parentizacao:
                lexema = lexema + codigo[j]
                if j+1 < len(codigo):
                    #verifica se juntando o prox caracter com o atual forma um atribuidor duplo
                    if lexema + codigo[j+1] in atribuidores_duplos:
                        continue
            #verifica se o caracter atual é um numero e se o lexema esta vazio
            elif codigo[j].isnumeric() and lexema == '':
                lexema = lexema + codigo[j]
                if j+1 < len(codigo):
                    if codigo[j+1].isnumeric() or codigo[j+1] == '.':
                        continue
                    #se o prox caracter for vazio ou um atribuidor ou parentes, salva 
                    if codigo[j+1] == ' ' or codigo[j+1] in atribuidores_parentizacao:
                        #verifica se é float
                        if '.' in lexema:
                            for key, value in valores_dos_dados.items():
                                if key == 'numerofloat':
                                    tokens.append(value)
                                    codigos.append(lexema)
                                    linha.append(i)
                                    lexema = ''
                                    break
                        else:
                            for key, value in valores_dos_dados.items():
                                if key == 'numerointeiro':
                                    tokens.append(value)
                                    codigos.append(lexema)
                                    linha.append(i)
                                    lexema = ''
                                    break
                #salva caso o numero for o ultimo caracter da linha
                else:
                    if '.' in lexema:
                        for key, value in valores_dos_dados.items():
                            if key == 'numerofloat':
                                tokens.append(value)
                                codigos.append(lexema)
                                linha.append(i)
                                lexema = ''
                                break
                    else:
                        for key, value in valores_dos_dados.items():
                            if key == 'numerointeiro':
                                tokens.append(value)
                                codigos.append(lexema)
                                linha.append(i)
                                lexema = ''
                                break
            #verifica se o caracter atual inicia um texto
            elif codigo[j] in textos:
                is_text = True
            elif codigo[j] != ' ':
                lexema = lexema + codigo[j]
            else:
                lexema = ''
                
            #verifica se o lexema esta dentro do dicionario de atribuidores duplos    
            if lexema in atribuidores_duplos:
                for key, value in atribuidores_duplos.items():
                    if key == lexema:
                        tokens.append(value)
                        codigos.append(key)
                        linha.append(i)
                        lexema = ''
                        break
            #verifica se o lexema esta dentro do dicionario de atribuidores simples
            elif lexema in atribuidores_parentizacao:
                for key, value in atribuidores_parentizacao.items():
                    if key == lexema:
                        tokens.append(value)
                        codigos.append(key)
                        linha.append(i)
                        lexema = ''
                        break
            #verifica se o lexema esta dentro das palavras reservadas
            elif lexema in palavras_reservadas:
                for key, value in palavras_reservadas.items():
                    if key == lexema:
                        if j+1 < len(codigo):
                            if codigo[j+1] in atribuidores_parentizacao or codigo[j+1] == ' ':
                                tokens.append(value)
                                codigos.append(key)
                                linha.append(i)
                                lexema = ''
                            else:
                                textBoxResult.configure(state="normal")
                                textBoxResult.insert('end', f'Erro lexico - Linha {i} - posicao {len(lexema) - j}')
                                textBoxResult.configure(state="disabled")
                        else:
                            tokens.append(value)
                            codigos.append(key)
                            linha.append(i)
                            lexema = ''
                        break
            #verifica se é declaração de variavel
            elif j+1 < len(codigo):
                if codigo[j+1] == ',' or codigo[j+1] == ':':
                    for key, value in valores_dos_dados.items():
                        if key == 'nomevariavel':
                            tokens.append(value)
                            codigos.append(lexema)
                            linha.append(i)
                            lexema = ''
                            break
            #verifica se o lexema ja estra dentro dos codigos, se estiver salva novamente pq é variavel
            if lexema in codigos:
                    for key, value in valores_dos_dados.items():
                        if key == 'nomevariavel':
                            tokens.append(value)
                            codigos.append(lexema)
                            linha.append(i)
                            lexema = ''
                            break
                        
    #coloca o resultado da analise lexica no espaço destinado
    textBoxResult.configure(state="normal")
    for i in range(len(tokens)):
        textBoxResult.insert('end', f'Token: {tokens[i]} - Lexema {codigos[i]} - Linha: {linha[i]}\n')
    textBoxResult.configure(state="disabled")
    
def importar_arquivo():
    #pega o caminho do arquivo
    arquivo = filedialog.askopenfile(mode='r', initialdir='./Desktop', title='Selecione um arquivo', filetypes=([('Arquivos de Texto', '*.txt')]))
    
    #abre o arquivo
    conteudo = arquivo.read()
    
    #coloca o texto no textBox
    textBox.delete('1.0', 'end')
    textBox.insert('end', conteudo)
    #

#interface grafica
app = ctk.CTk()

app.title("Analisador Léxico")
app.geometry("1280x650")
app.grid_columnconfigure((0,1,2,3), weight=1)
app.grid_rowconfigure((0,1,2,3), weight=1)
app.resizable(False, False)

#area para escrever
label = ctk.CTkLabel(app, text="Código:")
label.grid(row=0, column=0, padx=10)
textBox = ctk.CTkTextbox(app)
textBox.grid(row=0, column=0, rowspan=3, columnspan=4, sticky="nsew", padx=(10, 300), pady=10)

#area para mostrar analise lexica
textBoxResult = ctk.CTkTextbox(app, state="disabled")
textBoxResult.grid(row=0, column=2, rowspan=3, columnspan=2, sticky="nsew", padx=(890, 10), pady=10)

btnAnalisar = ctk.CTkButton(app, text="Analisar", command=analisar)
btnAnalisar.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

btnImportar = ctk.CTkButton(app, text="Importar Arquivo", command=importar_arquivo)
btnImportar.grid(row=3, column=3, columnspan=2, sticky="nsew", padx=10, pady=10)

app.mainloop()