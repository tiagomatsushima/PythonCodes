
import random

a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))

lista = [a, b, c, d]
chosen = random.choice(lista)

print('O aluno escolhido foi {}'.format(chosen))
