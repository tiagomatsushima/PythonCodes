#Programa que analise o nome de uma pessoa

nome = str(input('Digite seu nome completo: ')).strip() #remove os espaços antes ou depois.
print('Analisando seu nome.......')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'. format(nome.lower()))
print('Seu nome possui ao todo {} letras'.format(len(nome) - nome.count(' '))) #elimina os espaços entre nomes

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0].upper(), len(separa[0])))
#pra fazer o separa ficar maiúscula, o .upper vem depois das chaves

print(nome[4:13])






