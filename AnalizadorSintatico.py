sentenca = [3,2,3, 1]
producoes = {1: [3,6,1], 
             2: [3, 7], 
             3: [7], 
             4:[2,3, 7], 
             5:[]}
pilha=[]
producaoInicial = 1;
inicioNaoTerminais = 6;

pilha = producoes.get(producaoInicial);
# Criação das tabelas  num de colunas     num de linhas
tabela = [[0 for _ in range(4)] for _ in range(4)]

# Colunas dos terminais
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
tabela[1][0]=5
tabela[2][0]=6
tabela[3][0]=7
#  Número das produções
tabela[1][1]=1
tabela[2][1]=2
tabela[2][2]=3
tabela[2][3]=3
tabela[3][2]=5
tabela[3][3]=4

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