print ("digite el tamaño de las filas y las columnas de la matriz")
tama=input()
suma=0
ptime = time.process_time()
for i in range (tama):
	for j in range (tama):
		print("ingrese los valores de la matriz")
		matriz[i][j] = input()
for i in range (tama):
	for j in range (tama):
		print(matriz[i][j])
print("\n")

for i in range (tama):
	for j in range(tama):
		if(j>i):
			suma+=matriz[i][j]
print( "La suma de los elementos de la submatriz triangular superior es : ", suma)
etime = time.process_time( )
return float(etime - ptime)


#include <stdio.h>
#include <stdlib.h> 
#int main(void){
#int tama,valor;
#printf("digite el tamaño de las filas y las columnas de la matriz");
#scanf("%d",&tama);
#int matriz[tama][tama];
#printf("ingrese los valores de la matriz");
#	for(int i=0;i<tama;i++){
#		for(int j=0;j<tama;j++){
#			matriz[i][j]=scanf("%d", &valor);
#		}
#	}

#for(int i=0;i<tama;i++){
#	for(int j=0;j<tama;j++){
#		printf(matriz[i][j]);
#	}
#}

#return EXIT_SUCCESS;
#}








