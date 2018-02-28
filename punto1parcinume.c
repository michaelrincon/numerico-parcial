void main(){
int matriz[][];
int i,j,n=3,suma=0,triangu_sup=1;
	for(i=0;i<n-1;i++)
	{
		for(j=n-1;j>0;j--)
		{
			if(matriz[i][j] == 0){
				suma = suma + matriz[i][j];
				triangu_sup *=1;
			}
			else
				triangu_sup *=0;
		}	
	}
}
