
etanol = float(input('Digite o valor do Etanol: '))

gasolina = float (input('Digite o valor da Gasolina: '))

bomPreco = gasolina * 0.7

if etanol <= bomPreco:
	print('Use etanol')
else:
	print('Use gasolina')