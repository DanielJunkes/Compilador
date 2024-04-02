import customtkinter as ctk

#lista para salvar os tokens e codigos
tokens = []
codigos = []
linha = []

#dicionario com as palavras reservadas
palavras_reservadas = {'while': 1, 'void': 2, 'string': 3, 'return': 4, 'main': 11, 'integer': 13, 'inicio': 14, 'if': 15, 
                       'for': 17, 'float': 18, 'fim': 19, 'else': 20, 'do': 21, 'count': 22, 'cin': 23, 'char': 24, 
                       'callfuncao': 25}

#dicionario com atribuidores e parentizacao
#nome provisório
atribuidores_parentizacao = {'>>': 26, '>=': 27, '>': 28, '==': 29, '=': 30, '<=': 31, '<<': 32, '<': 33, '++': 34, '+': 35, '{': 36,
                             '}': 37, ';': 38, ':': 39, '/': 40, ',': 41, '*': 42, '(': 43, ')': 44, '$': 45, '!=': 46, '--': 47, '-': 48}

def analisar():
    #pega o numero de linhas
    linhas = textBox.index('end-1c').split('.')[0]   
    for i in range(1, int(linhas)+1):
        lexema = ''
        #pega o texto que esta na linha
        codigo = textBox.get(f'{i}.0', f'{i}.end')
        print(codigo)
        #percorre o texto da linha
        for j in range(len(codigo)):
            print(j)
            if codigo[j] != ' ':
                    lexema = lexema + codigo[j]
            else:
                lexema = ''
            print(lexema)
            #verifica se o lexema esta dentro das palavras reservadas
            if lexema in palavras_reservadas:
                for key, value in palavras_reservadas.items():
                    if key == lexema:
                        tokens.append(value)
                        codigos.append(key)
                        linha.append(i)
                        lexema = ''
                        break
            #verifica se o lexama esta dentro dos atribuidores e parentizacao
            elif lexema in atribuidores_parentizacao:
                if j+1 < len(codigo):
                    #verificacao para atribuidores com mais de um caracter
                    if lexema == '>':
                        if codigo[j+1] == '>' or codigo[j+1] == '=':
                            continue
                    if lexema == '<':
                        if codigo[j+1] == '<' or codigo[j+1] == '=':
                            continue
                    if lexema == '=':
                        if codigo[j+1] == '=':
                            continue
                    if lexema == '+':
                        if codigo[j+1] == '+':
                            continue
                    if lexema == '-':
                        if codigo[j+1] == '-':
                            continue
                    if lexema == '!':
                        if codigo[j+1] == '=':
                            continue
                    if lexema == '/':
                        if codigo[j+1] == '/':
                            break
                for key, value in atribuidores_parentizacao.items():
                    if key == lexema:
                        tokens.append(value)
                        codigos.append(key)
                        linha.append(i)
                        lexema = ''
                        break
                    
    for i in range(len(tokens)):
        print(f'Token: {tokens[i]} - Lexema: {codigos[i]} - Linha: {linha[i]}')

#interface grafica
app = ctk.CTk()

app.title("Analisador Léxico")
app.geometry("1000x600")
app.grid_columnconfigure((0,1,2), weight=1)
app.grid_rowconfigure((0,1,2,3), weight=1)

#area para escrever
textBox = ctk.CTkTextbox(app)
textBox.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="nsew", padx=10, pady=10)

btnAnalisar = ctk.CTkButton(app, text="Analisar", command=analisar)
btnAnalisar.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

app.mainloop()