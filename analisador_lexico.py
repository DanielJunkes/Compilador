import customtkinter as ctk

#lista para salvar os tokens e codigos
codigos = []
tokens = []
linha = []

#dicionario com as palavras reservadas
palavras_reservadas = {'while': 1, 'void': 2, 'string': 3, 'return': 4, 'main': 11, 'integer': 13, 'inicio': 14, 'if': 15, 
                       'for': 17, 'float': 18, 'fim': 19, 'else': 20, 'do': 21, 'count': 22, 'cin': 23, 'char': 24, 
                       'callfuncao': 25}



def analisar():
    #pega o numero de linhas
    linhas = textBox.index('end-1c').split('.')[0]
    for i in range(1, int(linhas)+1):
        #pega o texto que esta na linha
        codigo = textBox.get(f'{i}.0', f'{i}.end')
        lexema = ''
        #percorre o texto da linha
        for j in range(len(codigo)):
            if codigo[j] != ' ':
                lexema = lexema + codigo[j]
            else:
                lexema = ''
            #verifica se o lexema esta dentro das palavras reservadas
            if lexema in palavras_reservadas:
                for key, value in palavras_reservadas.items():
                    if key == lexema:
                        tokens.append(key)
                        codigos.append(value)
                        linha.append(i)
            elif lexema == '':
                pass
    for i in range(len(tokens)):
        print(f'Token: {tokens[i]} - Codigo: {codigos[i]} - Linha: {linha[i]}')

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