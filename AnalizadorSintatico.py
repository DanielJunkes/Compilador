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

# Colunas dos não terminais
tabela[0][1]=3
tabela[0][2]=1
tabela[0][3]=2
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