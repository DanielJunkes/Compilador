import re

class AnalisadorLexico:
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

    tokens = []
    
    def __init__(self):
        pass
    
    #funcao para escrever o resultado da analise na tela
    def __escrever_textbox(self,  textBoxResult, texto=None, token=0, codigo=0, linha=0):
        textBoxResult.configure(state='normal')
        if token > 0:
            textBoxResult.insert('end', f'Token: {token} | Lexema: {codigo} | Linha: {linha}\n')
        if texto != None:
            textBoxResult.insert('end', f'{texto}\n')
        textBoxResult.configure(state='disabled')
    
    #funcao que ira verificar os numeros e salvar
    def __verificar_numeros(self, lexema, i, j, textBoxResult):
        if '-' in lexema:
            self.__escrever_textbox(texto=f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero negativo', textBoxResult=textBoxResult)
        elif '.' in lexema:
            numero_split = lexema.split('.')
            if len(numero_split[1]) > 2:
                self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero de casas decimais maior que o permitido', textBoxResult=textBoxResult)
            elif len(numero_split[0]) > 5:
                self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero maior que o permitido', textBoxResult=textBoxResult)
            else:
                token = self.valores_dos_dados.get('numerofloat')
                self.tokens.append([token, i, lexema])
                self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
        else:
            if len(lexema) > 5:
                self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Numero maior que o permitido', textBoxResult=textBoxResult)
            else:
                token = self.valores_dos_dados.get('numerointeiro')
                self.tokens.append([token, i, lexema])
                self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)

    def __verificar_variavel(self, lexema, i, j, textBoxResult):
        if len(lexema) > 10:
            self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel maior que o permitido', textBoxResult=textBoxResult)
        elif re.search(r'\d', lexema):
            self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel não pode conter numeros', textBoxResult=textBoxResult)
        else:
            if re.search(r'[@_!#$%|^&*()<>?/\\}{~:.]', lexema):
                self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - Nome de variavel não pode conter caracteres especiais', textBoxResult=textBoxResult)
            else:
                token = self.valores_dos_dados.get('nomevariavel')
                self.tokens.append([token, i, lexema])
                self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)

    def analisar(self, textBox, textBoxResult):
        #limpa os dados das listas
        self.tokens.clear()
        
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
                            self.__escrever_textbox(f'Aviso - Linha {i} - Comentario de bloco não foi iniciado', textBoxResult=textBoxResult)
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
                    if codigo[j] in self.textos:
                        is_text = False
                        if tipo_text == codigo[j]:
                            if codigo[j] == "'":
                                if len(lexema) > 1:
                                    self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - char deve ter apenas 1 caracter', textBoxResult=textBoxResult)
                                    lexema = ''
                            elif codigo[j] == '"':
                                if len(lexema) > 20:
                                    self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema) + 1} - string maior que o permitido (20 caracteres)', textBoxResult=textBoxResult)
                                    lexema = ''
                            if lexema != '':
                                    token = self.textos.get(codigo[j])
                                    self.tokens.append([token, i, lexema])
                                    self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
                                    lexema = ''
                        else:
                            self.__escrever_textbox(f'Erro - Linha {i} - Posicao {j - len(lexema)} - Textos devem começar e finalizar com o mesmo tipo de aspas', textBoxResult=textBoxResult)
                            lexema = ''
                        tipo_text = ''
                    else:
                        lexema = lexema + codigo[j]
                        continue
                #verifica se é um dos possiveis atribuidores ou parenteses 
                elif codigo[j] in self.atribuidores_parentizacao:
                    lexema = lexema + codigo[j]
                    if j+1 < len(codigo):
                        #verifica se juntando o prox caracter com o atual forma um atribuidor duplo
                        if lexema + codigo[j+1] in self.atribuidores_duplos:
                            continue
                        #verificacao para definir o simbolo - como subtracao ou numero negativo
                        if self.tokens != [] and codigo[j] == '-':
                            if self.tokens[-1] == 5 or self.tokens[-1] == 6:
                                pass
                            elif codigo[j+1].isnumeric():
                                continue
                        elif self.tokens == [] and codigo[j] == '-':
                            continue
                #verifica se o caracter atual é um numero
                elif codigo[j].isnumeric():
                    lexema = lexema + codigo[j]
                    if lexema.isnumeric() or '-' in lexema or '.' in lexema:
                        if j+1 < len(codigo):
                            if codigo[j+1].isnumeric() or codigo[j+1] == '.':
                                continue
                            #se o prox caracter for vazio ou um atribuidor ou parentes, salva 
                            if codigo[j+1] == ' ' or codigo[j+1] in self.atribuidores_parentizacao:
                                self.__verificar_numeros(lexema, i, j, textBoxResult)
                                lexema = ''
                        #salva caso o numero for o ultimo caracter da linha
                        else:
                            self.__verificar_numeros(lexema, i, j, textBoxResult)
                            lexema = ''
                #verifica se o caracter atual inicia um texto
                elif codigo[j] in self.textos:
                    is_text = True
                    tipo_text = codigo[j]
                elif codigo[j] != ' ':
                    lexema = lexema + codigo[j]
                else:
                    lexema = ''
                    continue
                    
                #verifica se o lexema esta dentro do dicionario de atribuidores duplos    
                if lexema in self.atribuidores_duplos:
                    token = self.atribuidores_duplos.get(lexema)
                    self.tokens.append([token, i, lexema])
                    self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
                    lexema = ''
                
                #verifica se o lexema esta dentro do dicionario de atribuidores simples
                elif lexema in self.atribuidores_parentizacao:
                    token = self.atribuidores_parentizacao.get(lexema)
                    self.tokens.append([token, i, lexema])
                    self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
                    lexema = ''
                    
                #verifica se o lexema esta dentro das palavras reservadas
                elif lexema in self.palavras_reservadas:
                    token = self.palavras_reservadas.get(lexema)
                    if j+1 < len(codigo):
                        if codigo[j+1] in self.atribuidores_parentizacao or codigo[j+1] == ' ':
                            self.tokens.append([token, i, lexema])
                            self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
                            lexema = ''
                        else:
                            continue
                    else:
                        self.tokens.append([token, i, lexema])
                        self.__escrever_textbox(token=token, codigo=lexema, linha=i, textBoxResult=textBoxResult)
                        lexema = ''
                        
                #verifica se é declaração de variavel
                elif lexema != '' and codigo[j] != '!':    
                    if j+1 < len(codigo):
                        if codigo[j+1] == ' ' or codigo[j+1] in self.atribuidores_parentizacao:
                            self.__verificar_variavel(lexema, i, j, textBoxResult)
                            lexema = ''
                    else:
                        self.__verificar_variavel(lexema, i, j, textBoxResult)
                        lexema = ''
        if is_text:
            self.__escrever_textbox(f'Erro - Um dado do tipo texto foi iniciado mas não finalizado', textBoxResult=textBoxResult)
        if comentario_bloco:
            self.__escrever_textbox(f'Erro - Um comentario de bloco foi iniciado mas não finalizado', textBoxResult=textBoxResult)
            
        return self.tokens
            
            