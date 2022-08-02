#programa que lê um nome e verifica se tem 'SILVA'

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) #procurar um nome dentro de outro


