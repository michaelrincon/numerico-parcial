def medidadetiempo(matriz, tama):
	ptime = time.process_time()
	matri(matriz, tama)
	etime = time.process_time( )
	return float(etime - ptime)


def matri(matriz, tama):
	for i in range (tama):
		for j in range (tama):
			print("ingrese los valores de la matriz")
			matriz[i][j] = input()
	for i in range (tama):
		for j in range (tama):
			print(matriz[i][j])
	print("\n")
	suma=0
	for i in range (tama):
		for j in range(tama):
			if(j>i):
				suma+=matriz[i][j]
		print( "La suma de los elementos de la submatriz triangular superior es : ", suma)



print ("digite el tamaño de las filas y las columnas de la matriz")
tama=input()
medidadetiempo(matriz,tama)

