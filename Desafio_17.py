#import math

#b = float(input('digite um valor: '))
#c = float(input('digite um valor: '))
#a = b.__pow__(2) + c.__pow__(2)

#print('O valor da hipotenusa é {}'.format(math.sqrt.(a)))


import math
co = float(input('digite um valor: '))
ca = float(input('digite um valor: '))
hi = math.hypot(co, ca)
print('O valor do cateto oposto é {}, o valor do cateto adjascente é {} e o valor da hipotenusa é {:.2f}'.format(co, ca, hi))
