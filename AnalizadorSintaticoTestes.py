sentenca = [3,2,3, 1]
producoes = { 1: [2, 11, 37, 50, 51, 52, 36], 
    2: [7, 53, 39, 54, 38, 55], 
    3: [16], 
    4: [16], 
    5: [41, 7, 53],
    6: [13], 
    7: [18], 
    8: [3], 
    9: [24], 
    10: [57, 39, 54, 38, 55],
    11: [16], 
    12: [7, 53], 
    13: [58, 7, 59, 37, 50,51, 52, 4, 44, 60, 43, 36, 51], 
    14: [13], 
    15: [2],
    16: [24], 
    17: [18], 
    18: [3], 
    19: [16], 
    20: [5],
    21: [6], 
    22: [7], 
    23: [8], 
    24: [10], 
    25: [16],
    26: [16], 
    27: [44, 61, 43], 
    28: [54, 7, 62], 
    29: [38, 54, 7, 62],
    30: [16],
    31: [14, 63, 38, 64,19], 
    32: [16], 
    33: [63, 38, 64], 
    34: [7, 30, 65], 
    35: [10, 30, 65],
    36: [8, 30, 65], 
    37: [16], 
    38: [25, 7, 66], 
    39: [16],
    40: [44, 67, 68, 43],
    41: [16], 
    42: [44, 67, 68, 43], 
    43: [5], 
    44: [10], 
    45: [6],
    46: [8], 
    47: [7], 
    48: [15, 44, 7, 69, 43, 37, 63, 38, 64, 36, 70] , 
    49: [20, 37, 63, 38, 64, 36], 
    50: [16],
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
    69: [16], 
    70: [32, 7, 74, 73],
    71: [16], 
    72: [41,7,74], 
    73: [77,78], 
    74: [25,7,66], 
    75: [35,77,78],
    76: [48,77,78], 
    77: [16], 
    78: [79,80], 
    79: [16], 
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
inicioNaoTerminais = 6

pilha = producoes.get(producaoInicial)

# Criação das tabelas  num de colunas     num de linhas
tabela = [[0 for _ in range(49)] for _ in range(33)]


# Colunas dos terminais
def completarMatriz():
    tabela[0][1]=2
    tabela[0][2]=11
    tabela[0][3]=37
    tabela[0][4]=36
    tabela[0][5]=7
    tabela[0][6]=39
    tabela[0][7]=38
    tabela[0][8]=41
    tabela[0][9]=13
    tabela[0][10]=18
    tabela[0][11]=3
    tabela[0][12]=24
    tabela[0][13]=4
    tabela[0][14]=44
    tabela[0][15]=43
    tabela[0][16]=5
    tabela[0][17]=6
    tabela[0][18]=8
    tabela[0][19]=10
    tabela[0][20]=14
    tabela[0][21]=19
    tabela[0][22]=30
    tabela[0][23]=25
    tabela[0][24]=15
    tabela[0][25]=20
    tabela[0][26]=1
    tabela[0][27]=29
    tabela[0][28]=46
    tabela[0][29]=28
    tabela[0][30]=27
    tabela[0][31]=33
    tabela[0][32]=31
    tabela[0][33]=17
    tabela[0][34]=34
    tabela[0][35]=47
    tabela[0][36]=21
    tabela[0][37]=23
    tabela[0][38]=26
    tabela[0][39]=22
    tabela[0][40]=32
    tabela[0][41]=12
    tabela[0][42]=35
    tabela[0][43]=48
    tabela[0][44]=42
    tabela[0][45]=40

    # Linha dos não terminais
    tabela[1][0]=49
    tabela[2][0]=50
    tabela[3][0]=53
    tabela[4][0]=54
    tabela[5][0]=55
    tabela[6][0]=57
    tabela[7][0]=51
    tabela[8][0]=58
    tabela[9][0]=60
    tabela[10][0]=59
    tabela[11][0]=61
    tabela[12][0]=62
    tabela[13][0]=52
    tabela[14][0]=64
    tabela[15][0]=63
    tabela[16][0]=66
    tabela[17][0]=68
    tabela[18][0]=67
    tabela[19][0]=70
    tabela[20][0]=69
    tabela[21][0]=71
    tabela[22][0]=72
    tabela[23][0]=73
    tabela[24][0]=74
    tabela[25][0]=65
    tabela[26][0]=78
    tabela[27][0]=77
    tabela[28][0]=80
    tabela[29][0]=79
    
    #  Número das produções
    tabela[1][1]=1
    tabela[2][1]=3
    tabela[5][1]=11
    tabela[7][1]=13
    tabela[8][1]=15
    tabela[10][3]=26
    tabela[14][4]=32
    tabela[2][5]=2
    tabela[5][5]=10
    tabela[6][5]=12
    tabela[9][5]=22
    tabela[14][5]=33
    tabela[15][5]=34
    tabela[18][5]=47
    tabela[21][5]=62
    tabela[25][5]=73
    tabela[27][5]=78
    tabela[29][5]=84
    tabela[3][6]=4
    tabela[12][7]=29
    tabela[14][7]=33
    tabela[15][7]=37
    tabela[16][7]=39
    tabela[19][7]=50
    tabela[23][7]=69
    tabela[24][7]=71
    tabela[26][7]=77
    tabela[28][7]=79
    tabela[3][8]=5
    tabela[17][8]=42
    tabela[24][8]=72
    tabela[2][9]=3
    tabela[4][9]=6
    tabela[5][9]=11
    tabela[7][9]=13
    tabela[8][9]=14
    tabela[11][9]=28
    tabela[2][10]=3
    tabela[4][10]=7
    tabela[5][10]=11
    tabela[7][10]=13
    tabela[8][10]=17
    tabela[11][10]=28
    tabela[2][11]=3
    tabela[4][11]=8
    tabela[5][11]=11
    tabela[7][11]=13
    tabela[8][11]=18
    tabela[11][11]=28
    tabela[2][12]=3
    tabela[4][12]=9
    tabela[5][12]=11
    tabela[7][12]=13
    tabela[8][12]=16
    tabela[11][12]=28
    tabela[10][14]=27
    tabela[16][14]=40
    tabela[25][14]=73
    tabela[27][14]=78
    tabela[29][14]=87
    tabela[9][15]=25
    tabela[12][15]=30
    tabela[16][15]=39
    tabela[17][15]=41
    tabela[26][15]=77
    tabela[28][15]=79
    tabela[9][16]=20
    tabela[18][16]=43
    tabela[21][16]=58
    tabela[25][16]=73
    tabela[27][16]=78
    tabela[29][16]=82
    tabela[9][17]=21
    tabela[18][17]=45
    tabela[21][17]=59
    tabela[25][17]=73
    tabela[27][17]=78
    tabela[29][17]=83
    tabela[9][18]=23
    tabela[14][18]=33
    tabela[15][18]=36
    tabela[18][18]=46
    tabela[21][18]=61
    tabela[25][18]=73
    tabela[27][18]=78
    tabela[19][18]=86
    tabela[9][19]=24
    tabela[14][19]=33
    tabela[15][19]=35
    tabela[18][19]=44
    tabela[21][19]=60
    tabela[25][19]=73
    tabela[27][19]=78
    tabela[29][19]=85
    tabela[2][20]=3
    tabela[5][20]=11
    tabela[7][20]=19
    tabela[13][20]=31
    tabela[14][21]=32
    tabela[14][23]=33
    tabela[15][23]=38
    tabela[25][23]=74
    tabela[14][24]=33
    tabela[15][24]=48
    tabela[19][25]=49
    tabela[14][26]=33
    tabela[15][26]=51
    tabela[20][27]=52
    tabela[20][28]=53
    tabela[20][29]=54
    tabela[20][30]=55
    tabela[20][31]=56
    tabela[20][32]=57
    tabela[14][33]=33
    tabela[15][33]=63
    tabela[22][34]=64
    tabela[22][35]=65
    tabela[14][36]=33
    tabela[15][36]=66
    tabela[14][37]=33
    tabela[15][37]=67
    tabela[14][39]=33
    tabela[15][39]=68
    tabela[23][40]=70
    tabela[24][40]=71
    tabela[26][42]=75
    tabela[28][42]=79
    tabela[26][43]=76
    tabela[28][43]=79
    tabela[28][44]=80
    tabela[28][45]=81

completarMatriz()

def acharNumProducao(naoTerminal, terminal):
    numeroProducao=tabela[naoTerminal][terminal]
    # print(naoTerminal, terminal)
    # print(numeroProducao)
    return numeroProducao

pilhaAnterior=[]
umaVez=False

while True:
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
        
        # print(linhaNaoTerminal, colunaTerminal)
        numeroProducao = acharNumProducao(linhaNaoTerminal, colunaTerminal)
        adicionarAPilha = producoes.get(numeroProducao) 
        pilha.pop(0)
        pilha = adicionarAPilha + pilha
        
    elif pilha[0] == sentenca[0]:
        pilha.pop(0)
        sentenca.pop(0)
    
    if umaVez:
        break
    if pilha == pilhaAnterior:
        umaVez = True
    if not sentenca:
        break
    pilhaAnterior=pilha



#  testes:
# if __name__ == "__main__":
#     analizadorSintatico()
    

    # print(pilha)
    # if pilha[0] == sentenca[0]:
    #     pilha.pop(0)
    #     sentenca.pop(0)
    # print(pilha)
    # if pilha[0] >= inicioNaoTerminais:
    #     linhaNaoTerminal=0;
    #     linhaTerminal=0;
    #     i=0;
        
    #     for linha in tabela:
    #         if i == 0:
    #             linhaTerminal = linha.index(3)
    #         if linha[0] == pilha[0]:
    #             linhaNaoTerminal = i;
    #         i += 1;
            
    #     print(linhaNaoTerminal, linhaTerminal)
    #     numeroProducao = acharNumProducao(linhaNaoTerminal, linhaTerminal)
    #     print(numeroProducao)
    #     adicionarAPilha = producoes.get(numeroProducao) 
    #     pilha.pop(0)
    #     pilha = adicionarAPilha + pilha


print(f"pilha:{pilha} \nsentenca: {sentenca} \n")