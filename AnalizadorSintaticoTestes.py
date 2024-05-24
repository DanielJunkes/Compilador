
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
    24: [ ], 
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
    42: [44, 67, 68, 43], 
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

pilha=[]
producaoInicial = 1
inicioNaoTerminais = 49

# Criação das tabelas  num de colunas     num de linhas
tabela = [[0 for _ in range(49)] for _ in range(33)]


# Colunas dos terminais
def completarMatriz():
    tabela[0][1]=1
    tabela[0][2]=2
    tabela[0][3]=3
    tabela[0][4]=4
    tabela[0][5]=5
    tabela[0][6]=6
    tabela[0][7]=7
    tabela[0][8]=8
    tabela[0][9]=9
    tabela[0][10]=10
    tabela[0][11]=11
    tabela[0][12]=12
    tabela[0][13]=13
    tabela[0][14]=14
    tabela[0][15]=15
    tabela[0][16]=16
    tabela[0][17]=17
    tabela[0][18]=18
    tabela[0][19]=19
    tabela[0][20]=20
    tabela[0][21]=21
    tabela[0][22]=22
    tabela[0][23]=23
    tabela[0][24]=24
    tabela[0][25]=25
    tabela[0][26]=26
    tabela[0][27]=27
    tabela[0][28]=28
    tabela[0][29]=29
    tabela[0][30]=30
    tabela[0][31]=31
    tabela[0][32]=32
    tabela[0][33]=33
    tabela[0][34]=34
    tabela[0][35]=35
    tabela[0][36]=36
    tabela[0][37]=37
    tabela[0][38]=38
    tabela[0][39]=39
    tabela[0][40]=40
    tabela[0][41]=41
    tabela[0][42]=42
    tabela[0][43]=43
    tabela[0][44]=44
    tabela[0][45]=45
    tabela[0][46]=46
    tabela[0][47]=47
    tabela[0][48]=48
    
    # Linha dos não terminais
    tabela[1][0]=49
    tabela[2][0]=50
    tabela[3][0]=51
    tabela[4][0]=52
    tabela[5][0]=53
    tabela[6][0]=54
    tabela[7][0]=55
    tabela[8][0]=57
    tabela[9][0]=58
    tabela[10][0]=59
    tabela[11][0]=60
    tabela[12][0]=61
    tabela[13][0]=62
    tabela[14][0]=63
    tabela[15][0]=64
    tabela[16][0]=65
    tabela[17][0]=66
    tabela[18][0]=67
    tabela[19][0]=68
    tabela[20][0]=69
    tabela[21][0]=70
    tabela[22][0]=71
    tabela[23][0]=72
    tabela[24][0]=73
    tabela[25][0]=74
    tabela[26][0]=77
    tabela[27][0]=78
    tabela[28][0]=79
    tabela[29][0]=80
    
    #  Número das produções
    
    #bloco 49 
    tabela[1][2]=1 
    
    #dclvar 50
    tabela[2][2]=3 
    tabela[2][7]=2
    tabela[2][13]=3
    tabela[2][18]=3
    tabela[2][3]=3
    tabela[2][24]=3
    tabela[2][14]=3
    
    #dclfunc 51
    tabela[3][2]=13
    tabela[3][13]=13
    tabela[3][18]=13
    tabela[3][3]=13
    tabela[3][24]=13
    tabela[3][14]=19
    
    #corpo 52
    tabela[4][14]=31
    
    #repident 53
    tabela[5][39]=4
    tabela[5][41]=5
    
    #tipo 54
    tabela[6][13]=6 
    tabela[6][18]=7
    tabela[6][3]=8
    tabela[6][24]=9
    
    #ldvar 55
    tabela[7][2]=11 
    tabela[7][7]=10
    tabela[7][13]=11
    tabela[7][18]=11
    tabela[7][13]=11
    tabela[7][24]=11
    tabela[7][14]=11
    
    #lid 57
    tabela[8][7]=12 

    #tipo_retorno 58
    tabela[9][2]=15
    tabela[9][13]=14
    tabela[9][18]=17
    tabela[9][3]=18
    tabela[9][24]=16
    
    #defpar 59
    tabela[10][37]=26
    tabela[10][44]=27
    
    #valor_retorno 60
    tabela[11][7]=22
    tabela[11][43]=25
    tabela[11][5]=20
    tabela[11][6]=21
    tabela[11][8]=23
    tabela[11][10]=24
    
    #param 61
    tabela[12][13]=28
    tabela[12][18]=28
    tabela[12][3]=28
    tabela[12][24]=28
    
    #lparam 62
    tabela[13][38]=29
    tabela[13][14]=30
    
    #comando 63
    tabela[14][7]=34
    tabela[14][38]=37
    tabela[14][8]=36
    tabela[14][10]=35
    tabela[14][25]=38
    tabela[14][15]=48
    tabela[14][1]=51
    tabela[14][17]=63
    tabela[14][21]=66
    tabela[14][23]=67
    tabela[14][22]=68
    
    #repcomando 64
    tabela[15][36]=32
    tabela[15][7]=33
    tabela[15][38]=33
    tabela[15][8]=33
    tabela[15][10]=33
    tabela[15][19]=32
    tabela[15][25]=33
    tabela[15][15]=33
    tabela[15][1]=33
    tabela[15][17]=33
    tabela[15][21]=33
    tabela[15][23]=33
    tabela[15][22]=33
    
    #expressao 65
    tabela[16][7]=73
    tabela[16][44]=73
    tabela[16][5]=73
    tabela[16][6]=73
    tabela[16][8]=73
    tabela[16][10]=73
    tabela[16][25]=74
    
    #parametros 66
    tabela[17][38]=39
    tabela[17][44]=40
    tabela[17][43]=39

    #tparam 67
    tabela[18][7]=47
    tabela[18][5]=43
    tabela[18][6]=45
    tabela[18][8]=46
    tabela[18][10]=44
    
    #reppar 68
    tabela[19][41]=42
    tabela[19][43]=41
    
    #comparacao 69
    tabela[20][29]=52
    tabela[20][46]=53
    tabela[20][28]=54
    tabela[20][27]=55
    tabela[20][33]=56
    tabela[20][31]=57
    
    #elseparte 70
    tabela[21][38]=50
    tabela[21][20]=49

    #contcomparcao 71
    tabela[22][7]=62
    tabela[22][5]=58
    tabela[22][6]=59
    tabela[22][8]=61
    tabela[22][10]=60
    
    #incremento 72
    tabela[23][34]=64
    tabela[23][47]=65
    
    #seqcount 73
    tabela[24][38]=69
    tabela[24][32]=70
    
    #sequencia 74
    tabela[25][38]=71
    tabela[25][41]=72
    tabela[25][32]=71
    
    #termo 77
    tabela[26][7]=78
    tabela[26][44]=78
    tabela[26][5]=78
    tabela[26][6]=78
    tabela[26][8]=78
    tabela[26][10]=78
    
    #repexp 78
    tabela[27][38]=77
    tabela[27][43]=77
    tabela[27][35]=75
    tabela[27][48]=76
    
    #fator 79
    tabela[28][7]=84
    tabela[28][44]=87
    tabela[28][5]=82
    tabela[28][6]=83
    tabela[28][8]=86
    tabela[28][10]=85
    
    #reptermo 80
    tabela[29][38]=79
    tabela[29][43]=79
    tabela[29][35]=79
    tabela[29][48]=79
    tabela[29][42]=80
    tabela[29][40]=81

completarMatriz()


pilha = producoes.get(producaoInicial) + ["$"]
# sentenca = [2, 11, 37, 7, 39, 13, 38, 14, 8, 30, 10, 42, 8, 38, 19, 36]
# sentenca = [2, 11, 37,14, 7, 30, 25,7, 38, 19, 36]
# sentenca = [2, 11, 37, 14, 7, 30, 25,7, 38, 19, 36]
# sentenca = [2, 11, 37, 14, 38, 19, 36]
senteca = []

def acharNumProducao(naoTerminal, terminal):
    numeroProducao=tabela[naoTerminal][terminal]
    return numeroProducao

    
while pilha[0] != "$":
    
    print(f"pilha:{pilha} \nsentenca: {sentenca}\n")
    
    if pilha[0] >= inicioNaoTerminais:
        linhaNaoTerminal=0
        colunaTerminal=0
        i=0
        
        for linha in tabela:
            if i == 0:
                colunaTerminal = linha.index(sentenca[0])
            if linha[0] == pilha[0]:
                linhaNaoTerminal = i
            i += 1
        
        print(acharNumProducao(linhaNaoTerminal, colunaTerminal), "\n")
        numeroProducao = acharNumProducao(linhaNaoTerminal, colunaTerminal)
        adicionarAPilha = producoes.get(numeroProducao) 
        pilha.pop(0)
        pilha = adicionarAPilha + pilha
        
    elif pilha[0] == sentenca[0]:
        pilha.pop(0)
        sentenca.pop(0)
    else:
        break

if pilha[0] == "$":
    print("Sintaxe correta")
else:
    print("Erro sintático")