import re
import customtkinter as ctk
from tkinter import filedialog
from AnalisadorSintatico import AnalisadorSintatico
#dicionario com as palavras reservadas
palavras_reservadas = {'while': 1, 'void': 2, 'string': 3, 'return': 4, 'main': 11, 'literal': 12, 'integer': 13, 'inicio': 14, 'if': 15, 
                       'for': 17, 'float': 18, 'fim': 19, 'else': 20, 'do': 21, 'cout': 22, 'cin': 23, 'char': 24, 
                       'callfuncao': 25}
#dicionario com atribuidores e parentizacao
atribuidores_parentizacao = {'>': 28, '=': 30, '<': 33, '+': 35, '}': 36, '{': 37, ';': 38, ':': 39, 
                             '/': 40, ',': 41, '*': 42, ')': 43, '(': 44, '$': 45, '-': 48}
atribuidores_duplos = {'>>': 26, '>=': 27, '==': 29, '<=': 31, '<<': 32,'++': 34, '!=': 46, '--': 47}
#dicionario com os tokens dos valores dos dados
valores_dos_dados = {'numerointeiro': 5, 'numerofloat': 6, 'nomevariavel': 7, 'nomedochar': 8, 'nomedastring': 10}
#dicionatio com simbolos que iniciam textos
textos = {'"': 10, "'": 8, '|': 12} #10 string, 8 char e 12 literal

#lista com os codigos
tokens = []

#funcao para escrever o resultado da analise na tela
def escrever_textbox(texto=None, token=0, codigo=0, linha=0):
    textBoxResult.configure(state='normal')
    if token > 0:
        textBoxResult.insert('end', f'Token: {token} | Lexema: {codigo} | Linha: {linha}\n')
    if texto != None:
        textBoxResult.insert('end', f'{texto}\n')
    textBoxResult.configure(state='disabled')

#funcao que ira verificar os numeros e salvar
def verificar_numeros(lexema, i, j):
    if '-' in lexema:
        escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero negativo')
    elif '.' in lexema:
        numero_split = lexema.split('.')
        if len(numero_split[1]) > 2:
            escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero de casas decimais maior que o permitido')
        elif len(numero_split[0]) > 5:
            escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero maior que o permitido')
        else:
            token = valores_dos_dados.get('numerofloat')
            tokens.append([token, i, j-len(lexema)+1])
            escrever_textbox(token=token, codigo=lexema, linha=i)
    else:
        if len(lexema) > 5:
            escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero maior que o permitido')
        else:
            token = valores_dos_dados.get('numerointeiro')
            tokens.append([token, i, j-len(lexema)+1])
            escrever_textbox(token=token, codigo=lexema, linha=i)

def verificar_variavel(lexema, i, j):
    if len(lexema) > 10:
        escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel maior que o permitido')
    elif re.search(r'\d', lexema):
        escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel não pode conter numeros')
    else:
        if re.search(r'[@_!#$%|^&*()<>?/\\}{~:.]', lexema):
            escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel não pode conter caracteres especiais')
        else:
            token = valores_dos_dados.get('nomevariavel')
            tokens.append([token, i, j-len(lexema)+1])
            escrever_textbox(token=token, codigo=lexema, linha=i)
            

def analisar():
    #limpa os dados das listas
    tokens.clear()
    
    #variaveis de controle
    comentario_bloco = False
    is_text = False
    #saber qual tipo de aspas foi aberta
    tipo_text = ''

    #limpa o espaço para mostrar o resultado da analise lexica
    textBoxResult.configure(state="normal")
    textBoxResult.delete('1.0', 'end')
    textBoxResult.configure(state="disabled")
    
    #pega o numero de linhas
    linhas = textBox.index('end-1c').split('.')[0]
    lexema = ''
    
    for i in range(1, int(linhas)+1):
        #pega o texto que esta na linha
        codigo = textBox.get(f'{i}.0', f'{i}.end').strip('\t')
       
        #percorre o texto da linha  
        for j in range(len(codigo)):
            #parte dos comentarios
            #verifica se tem *\ na linha do para finalizar o comentario em bloco caso esteja em comentario
            if '*\\' in codigo:
                    if comentario_bloco:
                        comentario_bloco = False
                        break
                    else:
                        escrever_textbox(f'Aviso - Linha {i} - Comentario de bloco não foi iniciado')
                        codigo = codigo.replace('*\\', '  ')
            if comentario_bloco:
                break
            if codigo[j] == '\\':
                if j+1 < len(codigo):
                    if codigo[j+1] == '\\':
                        break
                    if codigo[j+1] == '*':
                        comentario_bloco = True
                        break
            #parte da string, char e literal
            elif is_text:
                if codigo[j] in textos:
                    is_text = False
                    if tipo_text == codigo[j]:
                        if codigo[j] == "'":
                            if len(lexema) > 1:
                                escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - char deve ter apenas 1 caracter')
                                lexema = ''
                        elif codigo[j] == '"':
                            if len(lexema) > 20:
                                escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - string maior que o permitido (20 caracteres)')
                                lexema = ''
                        if lexema != '':
                                token = textos.get(codigo[j])
                                tokens.append([token, i, j-len(lexema)+1])
                                escrever_textbox(token=token, codigo=lexema, linha=i)
                                lexema = ''
                    else:
                        escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema)} - Textos devem começar e finalizar com o mesmo tipo de aspas')
                        lexema = ''
                    tipo_text = ''
                else:
                    lexema = lexema + codigo[j]
                    continue
            #verifica se é um dos possiveis atribuidores ou parenteses 
            elif codigo[j] in atribuidores_parentizacao:
                lexema = lexema + codigo[j]
                if j+1 < len(codigo):
                    #verifica se juntando o prox caracter com o atual forma um atribuidor duplo
                    if lexema + codigo[j+1] in atribuidores_duplos:
                        continue
                    #verificacao para definir o simbolo - como subtracao ou numero negativo
                    if tokens != [] and codigo[j] == '-':
                        if tokens[-1] == 5 or tokens[-1] == 6:
                            pass
                        elif codigo[j+1].isnumeric():
                            continue
                    elif tokens == [] and codigo[j] == '-':
                        continue
            #verifica se o caracter atual é um numero
            elif codigo[j].isnumeric():
                lexema = lexema + codigo[j]
                if lexema.isnumeric() or '-' in lexema or '.' in lexema:
                    if j+1 < len(codigo):
                        if codigo[j+1].isnumeric() or codigo[j+1] == '.':
                            continue
                        #se o prox caracter for vazio ou um atribuidor ou parentes, salva 
                        if codigo[j+1] == ' ' or codigo[j+1] in atribuidores_parentizacao:
                            verificar_numeros(lexema, i, j)
                            lexema = ''
                    #salva caso o numero for o ultimo caracter da linha
                    else:
                        verificar_numeros(lexema, i, j)
                        lexema = ''
            #verifica se o caracter atual inicia um texto
            elif codigo[j] in textos:
                is_text = True
                tipo_text = codigo[j]
            elif codigo[j] != ' ':
                lexema = lexema + codigo[j]
            else:
                lexema = ''
                continue
                
            #verifica se o lexema esta dentro do dicionario de atribuidores duplos    
            if lexema in atribuidores_duplos:
                token = atribuidores_duplos.get(lexema)
                tokens.append([token, i, j-len(lexema)+1])
                escrever_textbox(token=token, codigo=lexema, linha=i)
                lexema = ''
            
            #verifica se o lexema esta dentro do dicionario de atribuidores simples
            elif lexema in atribuidores_parentizacao:
                token = atribuidores_parentizacao.get(lexema)
                tokens.append([token, i, j-len(lexema)+1])
                escrever_textbox(token=token, codigo=lexema, linha=i)
                lexema = ''
                
            #verifica se o lexema esta dentro das palavras reservadas
            elif lexema in palavras_reservadas:
                token = palavras_reservadas.get(lexema)
                if j+1 < len(codigo):
                    if codigo[j+1] in atribuidores_parentizacao or codigo[j+1] == ' ':
                        tokens.append([token, i, j-len(lexema)+1])
                        escrever_textbox(token=token, codigo=lexema, linha=i)
                        lexema = ''
                    else:
                        continue
                else:
                    tokens.append([token, i, j-len(lexema)+1])
                    escrever_textbox(token=token, codigo=lexema, linha=i)
                    lexema = ''
                    
            #verifica se é declaração de variavel
            elif lexema != '' and codigo[j] != '!':    
                if j+1 < len(codigo):
                    if codigo[j+1] == ' ' or codigo[j+1] in atribuidores_parentizacao:
                        verificar_variavel(lexema, i, j)
                        lexema = ''
                else:
                    verificar_variavel(lexema, i, j)
                    lexema = ''
    if is_text:
        escrever_textbox(f'Erro - Um dado do tipo texto foi iniciado mas não finalizado')
    if comentario_bloco:
        escrever_textbox(f'Erro - Um comentario de bloco foi iniciado mas não finalizado')
        
    analisadorSintatico = AnalisadorSintatico()
    analisadorSintatico.analisar(entrada=tokens, text_box=textBoxSintatico)
    
    
def importar_arquivo():
    #pega o caminho do arquivo
    arquivo = filedialog.askopenfile(mode='r', initialdir='./Desktop', title='Selecione um arquivo', filetypes=([('Arquivos de Texto', '*.txt')]))
    
    #abre o arquivo
    conteudo = arquivo.read()
    
    #coloca o texto no textBox
    textBox.delete('1.0', 'end')
    textBox.insert('end', conteudo)
    

#interface grafica
app = ctk.CTk()

app.title("Analisador Léxico")
app.geometry("1280x650")
app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

#area para escrever
label = ctk.CTkLabel(app, text="Código:")
label.grid(row=0, column=0, padx=10)
textBox = ctk.CTkTextbox(app)
textBox.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew", padx=(10, 10), pady=10)


#area para mostrar analise lexica
textBoxResult = ctk.CTkTextbox(app, state="disabled")
textBoxResult.grid(row=0, column=4, rowspan=2, sticky="nsew", padx=(0, 10), pady=(10, 0))

#area para mostrar analise sintatica
textBoxSintatico = ctk.CTkTextbox(app, state="disabled")
textBoxSintatico.grid(row=2, column=4, rowspan=2, sticky="nsew", padx=(0, 10), pady=10)

#botao d analisar
btnAnalisar = ctk.CTkButton(app, text="Analisar", command=analisar)
btnAnalisar.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

#botao para importar arquivo
btnImportar = ctk.CTkButton(app, text="Importar Arquivo", command=importar_arquivo)
btnImportar.grid(row=4, column=3, columnspan=3, sticky="nsew", padx=10, pady=10)

app.mainloop()