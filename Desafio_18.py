#import math

#a = float(input('Digite o valor do ângulo desejado: '))
#sen = math.sin(math.radians(a))
#cos = math.cos(math.radians(a))
#tan = math.tan(math.radians(a))

#print('Para o ângulo de {}, o valor do seno é {:.2f}, o valor do cosseno é {:.2f} e o valor da tangente é {:.2f}'.format(a, sen, cos, tan))


from math import radians, sin, cos, tan

a = float(input('Digite o ângulo desejado: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))

print('Para o ângulo de {}, o valor do seno é {:.2f}, o valor do cosseno é {:.2f} e o valor da tangente é {:.2f}'.format(a, seno, cosseno, tangente))
