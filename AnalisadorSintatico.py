class AnalisadorSintatico:
    
    producoes = { 1: [2, 11, 37, 50, 51, 52, 36], 
        2: [7, 53, 39, 54, 38, 55], 
        3: [ ], 
        4: [ ], 
        5: [41, 7, 53],
        6: [13], 
        7: [18], 
        8: [3], 
        9: [24], 
        10: [57, 39, 54, 38, 55],
        11: [ ], 
        12: [7, 53], 
        13: [58, 7, 59, 37, 50,51, 52, 4, 44, 60, 43, 36, 51], 
        14: [13], 
        15: [2],
        16: [24], 
        17: [18], 
        18: [3], 
        19: [ ], 
        20: [5],
        21: [6], 
        22: [7], 
        23: [8], 
        24: [10], 
        25: [ ],
        26: [ ], 
        27: [44, 61, 43], 
        28: [54, 7, 62], 
        29: [38, 54, 7, 62],
        30: [ ],
        31: [14, 63, 38, 64,19], 
        32: [ ], 
        33: [63, 38, 64], 
        34: [7, 30, 65], 
        35: [10, 30, 65],
        36: [8, 30, 65], 
        37: [ ], 
        38: [25, 7, 66], 
        39: [ ],
        40: [44, 67, 68, 43],
        41: [ ], 
        42: [41, 67, 68], 
        43: [5], 
        44: [10], 
        45: [6],
        46: [8], 
        47: [7], 
        48: [15, 44, 7, 69, 43, 37, 63, 38, 64, 36, 70] , 
        49: [20, 37, 63, 38, 64, 36], 
        50: [ ],
        51: [1, 44, 7, 69, 43, 37, 63, 38, 64, 36], 
        52: [29, 71], 
        53: [46, 71], 
        54: [28, 71], 
        55: [27, 71],
        56: [33, 71], 
        57: [31, 71], 
        58: [5], 
        59: [6], 
        60: [10],
        61: [8], 
        62: [7], 
        63: [17, 44, 7, 30, 71, 38, 7, 69, 38, 72, 43, 37, 63, 38, 64, 36], 
        64: [34, 5], 
        65: [47, 5],
        66: [21, 37, 63, 38, 64, 36, 1, 44, 7, 69, 43], 
        67: [23, 26, 7], 
        68: [22, 32, 12, 73], 
        69: [ ], 
        70: [32, 7, 74, 73],
        71: [ ], 
        72: [41,7,74], 
        73: [77,78], 
        74: [25,7,66], 
        75: [35,77,78],
        76: [48,77,78],
        77: [ ], 
        78: [79,80], 
        79: [ ], 
        80: [42,79,80],
        81: [40,79,80], 
        82: [5], 
        83: [6], 
        84: [7], 
        85: [10],
        86: [8], 
        87: [44, 65, 43]}
    
    producaoInicial = 1
    inicioNaoTerminais = 49

    # Criação das tabelas  num de colunas     num de linhas
    tabela = [[0 for _ in range(49)] for _ in range(33)]
    
    def __init__(self):
        self.__iniciarMatriz()
    
    def __iniciarMatriz(self):
        self.tabela[0][1]=1
        self.tabela[0][2]=2
        self.tabela[0][3]=3
        self.tabela[0][4]=4
        self.tabela[0][5]=5
        self.tabela[0][6]=6
        self.tabela[0][7]=7
        self.tabela[0][8]=8
        self.tabela[0][9]=9
        self.tabela[0][10]=10
        self.tabela[0][11]=11
        self.tabela[0][12]=12
        self.tabela[0][13]=13
        self.tabela[0][14]=14
        self.tabela[0][15]=15
        self.tabela[0][16]=16
        self.tabela[0][17]=17
        self.tabela[0][18]=18
        self.tabela[0][19]=19
        self.tabela[0][20]=20
        self.tabela[0][21]=21
        self.tabela[0][22]=22
        self.tabela[0][23]=23
        self.tabela[0][24]=24
        self.tabela[0][25]=25
        self.tabela[0][26]=26
        self.tabela[0][27]=27
        self.tabela[0][28]=28
        self.tabela[0][29]=29
        self.tabela[0][30]=30
        self.tabela[0][31]=31
        self.tabela[0][32]=32
        self.tabela[0][33]=33
        self.tabela[0][34]=34
        self.tabela[0][35]=35
        self.tabela[0][36]=36
        self.tabela[0][37]=37
        self.tabela[0][38]=38
        self.tabela[0][39]=39
        self.tabela[0][40]=40
        self.tabela[0][41]=41
        self.tabela[0][42]=42
        self.tabela[0][43]=43
        self.tabela[0][44]=44
        self.tabela[0][45]=45
        self.tabela[0][46]=46
        self.tabela[0][47]=47
        self.tabela[0][48]=48
        
        # Linha dos não terminais
        self.tabela[1][0]=49
        self.tabela[2][0]=50
        self.tabela[3][0]=51
        self.tabela[4][0]=52
        self.tabela[5][0]=53
        self.tabela[6][0]=54
        self.tabela[7][0]=55
        self.tabela[8][0]=57
        self.tabela[9][0]=58
        self.tabela[10][0]=59
        self.tabela[11][0]=60
        self.tabela[12][0]=61
        self.tabela[13][0]=62
        self.tabela[14][0]=63
        self.tabela[15][0]=64
        self.tabela[16][0]=65
        self.tabela[17][0]=66
        self.tabela[18][0]=67
        self.tabela[19][0]=68
        self.tabela[20][0]=69
        self.tabela[21][0]=70
        self.tabela[22][0]=71
        self.tabela[23][0]=72
        self.tabela[24][0]=73
        self.tabela[25][0]=74
        self.tabela[26][0]=77
        self.tabela[27][0]=78
        self.tabela[28][0]=79
        self.tabela[29][0]=80
        
        #  Número das produções
        
        #bloco 49 
        self.tabela[1][2]=1 
        
        #dclvar 50
        self.tabela[2][2]=3 
        self.tabela[2][7]=2
        self.tabela[2][13]=3
        self.tabela[2][18]=3
        self.tabela[2][3]=3
        self.tabela[2][24]=3
        self.tabela[2][14]=3
        
        #dclfunc 51
        self.tabela[3][2]=13
        self.tabela[3][13]=13
        self.tabela[3][18]=13
        self.tabela[3][3]=13
        self.tabela[3][24]=13
        self.tabela[3][14]=19
        
        #corpo 52
        self.tabela[4][14]=31
        
        #repident 53
        self.tabela[5][39]=4
        self.tabela[5][41]=5
        
        #tipo 54
        self.tabela[6][13]=6 
        self.tabela[6][18]=7
        self.tabela[6][3]=8
        self.tabela[6][24]=9
        
        #ldvar 55
        self.tabela[7][2]=11 
        self.tabela[7][7]=10
        self.tabela[7][13]=11
        self.tabela[7][18]=11
        self.tabela[7][13]=11
        self.tabela[7][24]=11
        self.tabela[7][14]=11
        
        #lid 57
        self.tabela[8][7]=12 

        #tipo_retorno 58
        self.tabela[9][2]=15
        self.tabela[9][13]=14
        self.tabela[9][18]=17
        self.tabela[9][3]=18
        self.tabela[9][24]=16
        
        #defpar 59
        self.tabela[10][37]=26
        self.tabela[10][44]=27
        
        #valor_retorno 60
        self.tabela[11][7]=22
        self.tabela[11][43]=25
        self.tabela[11][5]=20
        self.tabela[11][6]=21
        self.tabela[11][8]=23
        self.tabela[11][10]=24
        
        #param 61
        self.tabela[12][13]=28
        self.tabela[12][18]=28
        self.tabela[12][3]=28
        self.tabela[12][24]=28
        
        #lparam 62
        self.tabela[13][38]=29
        self.tabela[13][43]=30
        
        #comando 63
        self.tabela[14][7]=34
        self.tabela[14][38]=37
        self.tabela[14][8]=36
        self.tabela[14][10]=35
        self.tabela[14][25]=38
        self.tabela[14][15]=48
        self.tabela[14][1]=51
        self.tabela[14][17]=63
        self.tabela[14][21]=66
        self.tabela[14][23]=67
        self.tabela[14][22]=68
        
        #repcomando 64
        self.tabela[15][36]=32
        self.tabela[15][7]=33
        self.tabela[15][38]=33
        self.tabela[15][8]=33
        self.tabela[15][10]=33
        self.tabela[15][19]=32
        self.tabela[15][25]=33
        self.tabela[15][15]=33
        self.tabela[15][1]=33
        self.tabela[15][17]=33
        self.tabela[15][21]=33
        self.tabela[15][23]=33
        self.tabela[15][22]=33
        
        #expressao 65
        self.tabela[16][7]=73
        self.tabela[16][44]=73
        self.tabela[16][5]=73
        self.tabela[16][6]=73
        self.tabela[16][8]=73
        self.tabela[16][10]=73
        self.tabela[16][25]=74
        
        #parametros 66
        self.tabela[17][38]=39
        self.tabela[17][44]=40
        self.tabela[17][43]=39

        #tparam 67
        self.tabela[18][7]=47
        self.tabela[18][5]=43
        self.tabela[18][6]=45
        self.tabela[18][8]=46
        self.tabela[18][10]=44
        
        #reppar 68
        self.tabela[19][41]=42
        self.tabela[19][43]=41
        
        #comparacao 69
        self.tabela[20][29]=52
        self.tabela[20][46]=53
        self.tabela[20][28]=54
        self.tabela[20][27]=55
        self.tabela[20][33]=56
        self.tabela[20][31]=57
        
        #elseparte 70
        self.tabela[21][38]=50
        self.tabela[21][20]=49

        #contcomparcao 71
        self.tabela[22][7]=62
        self.tabela[22][5]=58
        self.tabela[22][6]=59
        self.tabela[22][8]=61
        self.tabela[22][10]=60
        
        #incremento 72
        self.tabela[23][34]=64
        self.tabela[23][47]=65
        
        #seqcount 73
        self.tabela[24][38]=69
        self.tabela[24][32]=70
        
        #sequencia 74
        self.tabela[25][38]=71
        self.tabela[25][41]=72
        self.tabela[25][32]=71
        
        #termo 77
        self.tabela[26][7]=78
        self.tabela[26][44]=78
        self.tabela[26][5]=78
        self.tabela[26][6]=78
        self.tabela[26][8]=78
        self.tabela[26][10]=78
        
        #repexp 78
        self.tabela[27][38]=77
        self.tabela[27][43]=77
        self.tabela[27][35]=75
        self.tabela[27][48]=76
        
        #fator 79
        self.tabela[28][7]=84
        self.tabela[28][44]=87
        self.tabela[28][5]=82
        self.tabela[28][6]=83
        self.tabela[28][8]=86
        self.tabela[28][10]=85
        
        #reptermo 80
        self.tabela[29][38]=79
        self.tabela[29][43]=79
        self.tabela[29][35]=79
        self.tabela[29][48]=79
        self.tabela[29][42]=80
        self.tabela[29][40]=81

        
    def __acharNumProducao(self, naoTerminal, terminal):
        numeroProducao=self.tabela[naoTerminal][terminal]
        return numeroProducao

    def analisar(self, entrada, text_box):
        
        text_box.configure(state="normal")
        text_box.delete('1.0', 'end')
        text_box.configure(state="disabled")
        
        pilha = self.producoes.get(self.producaoInicial) + ["$"]
        
        while pilha[0] != "$":
            
            tokens = []
            for i in range(len(entrada)):
                tokens.append(entrada[i][0])
    
            text_box.configure(state="normal")
            text_box.insert("end", f"pilha:{pilha} \nsentenca: {tokens}\n\n")
            text_box.configure(state="disabled")
                        
            if pilha[0] >= self.inicioNaoTerminais:
                
                linhaNaoTerminal=0
                colunaTerminal=0
                i=0
                
                for linha in self.tabela:
                    if i == 0:
                        colunaTerminal = linha.index(entrada[0][0])
                    if linha[0] == pilha[0]:
                        linhaNaoTerminal = i
                    i += 1
                
                numeroProducao = self.__acharNumProducao(linhaNaoTerminal, colunaTerminal)
                if numeroProducao == 0:
                    text_box.configure(state="normal")
                    text_box.insert("end", f"Erro lexico - Linha {entrada[0][1]} - Posição {entrada[0][2]}\n")
                    text_box.configure(state="disabled")
                    return 0
                adicionarAPilha = self.producoes.get(numeroProducao) 
                pilha.pop(0)
                pilha = adicionarAPilha + pilha
                
            elif pilha[0] == entrada[0][0]:
                pilha.pop(0)
                entrada.pop(0)
            else:
                text_box.configure(state="normal")
                text_box.insert("end", f"Erro lexico - Linha {entrada[0][1]} - Posição {entrada[0][2]}\n")
                text_box.configure(state="disabled")
                return 0
        
        text_box.configure(state="normal")
        text_box.insert("end", f"pilha:{pilha} \nsentenca: []\n")
        text_box.configure(state="disabled")
    
    