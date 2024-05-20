sentenca = [3,2,3, 1]
producoes = {1: [3,6,1], 3: [7], 4:[2,3]}
inicial = 1;
inicioNaoTerminais = 6;
                #      num de colunas      nume de linhas
tabela = [[0 for _ in range(4)] for _ in range(4)]

tabela[0][1]=1
tabela[0][2]=2
tabela[0][3]=3
tabela[1][0]=5
tabela[2][0]=6
tabela[3][0]=7

tabela[1][3]=1
tabela[2][1]=3
tabela[2][2]=3
tabela[2][3]=[2,3]
tabela[3][1]=5
tabela[3][2]=4
tabela[3][3]=4

for linha in tabela:
    print(linha)

pilha=[]

pilha = producoes.get(inicial);




# while True:
#     print(pilha)
    
    
#     if pilha[0] >= inicioNaoTerminais:
#         adicionarAPilha = producoes.get(pilha[0]) 
#         pilha.pop(0)
#         pilha = adicionarAPilha + pilha
#     elif pilha[0] == sentenca[0]:
#         pilha.pop(0)
#         sentenca.pop(0)
    

#     if not sentenca:
#         break


print(pilha) 

