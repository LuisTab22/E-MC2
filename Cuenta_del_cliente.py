# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	n = int()
	x = int()
	precio = float()
	total = float()
	print("Ingresar el total de artículos")
	n = int(input())
	x = 1
	total = 0
	while x<=n:
		print("Ingresar el precio del ",x)
		precio = float(input())
		total = total+precio
		x = x+1
	print("El total a pagar es: S/.",total)
	if x<3:
		print("Su pago debe ser en efectivo")
	else:
		print("Su pago debe ser con tarjeta")

