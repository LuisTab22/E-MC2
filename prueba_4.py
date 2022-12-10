# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	num = int()
	num = [int() for ind0 in range(5)]
	i = int()
	resultado = str()
	for i in range(1,6):
		# num(i)=azar(50)
		num[i-1] = int(input())
	for i in range(1,6):
		n = 1
		for j in range(1,6):
			if num[i-1]<=num[n-1]:
				n = j
		n1 = num[i-1]
		num[i-1] = num[n-1]
		num[n-1] = n1
	print("ARREGLO")
	print("")
	for i in range(1,6):
		valor = str(num[i-1])
		print(num[i-1])
		resultado = resultado+","+valor
	print("VALORES: ",resultado)

