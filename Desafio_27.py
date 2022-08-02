#Analisando o nome completo
nome = str(input('Digite seu nome completo: ')).upper().strip()
separa = nome.split()
#print(separa)
#print(separa[0])

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[len(separa)-1]))
#o comando separa[len(separa)-1] faz com que o computador conte o número de nomes que temos
#e faz o print do último nome da lista