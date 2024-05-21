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
producaoInicial = 1;
inicioNaoTerminais = 6;

pilha = producoes.get(producaoInicial);
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
    tabela[8][0]=56
    tabela[9][0]=57
    tabela[10][0]=58
    tabela[11][0]=59
    tabela[12][0]=60
    tabela[13][0]=61
    tabela[14][0]=62
    tabela[15][0]=63
    tabela[16][0]=64
    tabela[17][0]=65
    tabela[18][0]=66
    tabela[19][0]=67
    tabela[20][0]=68
    tabela[21][0]=69
    tabela[22][0]=70
    tabela[23][0]=71
    tabela[24][0]=72
    tabela[25][0]=73
    tabela[26][0]=74
    tabela[27][0]=75
    tabela[28][0]=76
    tabela[29][0]=77
    tabela[30][0]=78
    tabela[32][0]=79
    tabela[32][0]=80
    #  Número das produções
    tabela[1][2]=1
    tabela[2][2]=3
    tabela[2][3]=3
    tabela[2][13]=3
    tabela[2][16]=3
    tabela[2][18]=3
    tabela[2][24]=3
    tabela[3][2]=13
    tabela[3][3]=13
    tabela[3][13]=13
    tabela[3][14]=19
    # tabela[3][16]=19
    tabela[3][18]=13
    tabela[3][24]=13
    tabela[4][14]=31
    tabela[5][2]=4
    tabela[5][3]=4
    tabela[5][13]=4
    # tabela[5][16]=4
    tabela[5][18]=4
    tabela[5][24]=4
    tabela[5][39]=4
    tabela[5][41]=5
    tabela[6][3]=8
    tabela[6][9]=9
    tabela[6][13]=6
    tabela[6][18]=7
    tabela[7][2]=11
    tabela[7][3]=11
    tabela[7][9]=10
    tabela[7][13]=11
    tabela[7][16]=11
    tabela[7][18]=11
    tabela[7][24]=11
    tabela[9][7]=12
    tabela[10][2]=15
    tabela[10][3]=18
    tabela[10][13]=14
    tabela[10][18]=17
    tabela[10][24]=16
    # tabela[11][16]=26
    tabela[11][37]=26
    tabela[11][44]=27
    tabela[12][5]=20
    tabela[12][6]=21
    tabela[12][7]=22
    tabela[12][8]=23
    tabela[12][10]=24
    # tabela[12][16]=25
    tabela[12][43]=25
    tabela[13][13]=28
    tabela[13][18]=28
    tabela[13][24]=28
    tabela[14][16]=30
    tabela[14][38]=29
    tabela[14][43]=30
    tabela[15][1]=51
    tabela[15][7]=34
    tabela[15][8]=26
    tabela[15][10]=35
    tabela[15][15]=48
    # tabela[15][16]=37
    tabela[15][17]=63
    tabela[15][21]=68
    tabela[15][22]=68
    tabela[15][23]=68
    tabela[15][25]=39
    tabela[15][38]=37
    tabela[16][7]=33
    tabela[16][8]=33
    tabela[16][10]=33
    # tabela[16][16]=32
    tabela[16][19]=32
    tabela[16][25]=33
    tabela[16][36]=32
    tabela[17][5]=73
    tabela[17][6]=73
    tabela[17][8]=73
    tabela[17][9]=73
    tabela[17][25]=74
    tabela[17][44]=73
    # tabela[18][16]=39
    tabela[18][38]=39
    tabela[18][43]=39
    tabela[18][44]=40
    tabela[19][5]=43
    tabela[19][6]=45
    tabela[19][7]=47
    tabela[19][8]=46
    tabela[19][10]=44
    # tabela[20][16]=41
    tabela[20][38]=41
    tabela[20][43]=41
    tabela[20][44]=42
    tabela[21][27]=55
    tabela[21][28]=54
    tabela[21][29]=52
    tabela[21][31]=57
    tabela[21][33]=56
    tabela[21][46]=53
    # tabela[22][16]=50
    tabela[22][20]=49
    tabela[22][38]=50
    tabela[23][5]=58
    tabela[23][6]=59
    tabela[23][8]=61
    tabela[23][9]=62
    tabela[23][10]=60
    tabela[24][34]=64
    tabela[24][47]=65
    # tabela[25][16]=69
    tabela[25][32]=70
    tabela[25][38]=69
    # tabela[26][16]=71
    tabela[26][38]=71
    tabela[26][41]=72
    tabela[29][5]=78
    tabela[29][6]=78
    tabela[29][8]=78
    tabela[29][9]=78
    tabela[29][10]=78
    # tabela[30][16]=77
    tabela[30][35]=75
    tabela[30][38]=77
    tabela[30][43]=77
    tabela[30][44]=78
    tabela[30][48]=76
    tabela[31][5]=82
    tabela[31][6]=83
    tabela[31][7]=84
    tabela[31][8]=86
    tabela[31][10]=85
    tabela[31][44]=87
    # tabela[32][16]=79
    tabela[32][35]=79
    tabela[32][40]=81
    tabela[32][42]=80
    tabela[32][48]=79
   

completarMatriz()

def acharNumProducao(naoTerminal, terminal):
    numeroProducao=tabela[naoTerminal][terminal]
    # print(naoTerminal, terminal)
    # print(numeroProducao)
    return numeroProducao
pilhaAnterior=[]
umaVez=False;

    
while True:
    print(f"pilha:{pilha} \nsentenca: {sentenca}\n")
    
    if pilha[0] >= inicioNaoTerminais:
        linhaNaoTerminal=0;
        colunaTerminal=0;
        i=0;
        
        for linha in tabela:
            if i == 0:
                colunaTerminal = linha.index(sentenca[0])
            if linha[0] == pilha[0]:
                linhaNaoTerminal = i;
            i += 1;
        
        # print(linhaNaoTerminal, colunaTerminal)
        numeroProducao = acharNumProducao(linhaNaoTerminal, colunaTerminal)
        adicionarAPilha = producoes.get(numeroProducao) 
        pilha.pop(0)
        pilha = adicionarAPilha + pilha
        
    elif pilha[0] == sentenca[0]:
        pilha.pop(0)
        sentenca.pop(0)
    
    # if umaVez:
    #     break
    # if pilha == pilhaAnterior:
    #     umaVez = True
    if not sentenca:
        break
    # pilhaAnterior=pilha



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