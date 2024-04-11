texto = '1-1'
texto2 = '-1'
texto3 = 'num = -1'
texto4 = '1'
lexema = ''


teste = texto2
 
for i in range(len(teste)):
    if teste[i] == '-':
        if i+1 < len(teste):
            if teste[i+1].isnumeric() and teste[i+1].isnumeric():
                lexema = lexema+teste[i]  
                
                print('positivo')
            else:
                print('negativo')
    else:
        lexema = lexema+teste[i]
    

print(f'Lexema = {lexema}')

# if lexema.isnumeric():
#     print('positivo')
# else:
#     print('negativo')