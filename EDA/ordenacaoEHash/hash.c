#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int *criarVetor(int tam, int isRandom);
int *duplicarVetor(int *vetor,int size);
void printVetor(int *vetor, int tam);
void printTime(char* msg,int t);

int numeroDeDigitos(int num);
int ePotencia(int num, int base);

int metodoDivisao(int valorChave, int tamTAB);
//int metodoDobra(int valor, int tamTab);
int metodoMultiplicacao(int tam, int valor);
//int metodoAnaliseDigito();

void executeHashs(int *n, int sizeN);
int executeHashComDivisao(int *n, int *tabelaHash, int sizeN, int sizeTab);

int main(){
	srand(time(NULL));

	//int *n;
    int tamanhosDeN[]={200000,400000,600000,800000,1000000};

    for(int i=0;i<5;i++){
        int *n=criarVetor(tamanhosDeN[i], 1);
        executeHashs(n, tamanhosDeN[i]);
    }
    //printf("%d", metodoDobra(279384, 100));

    return 0;
}

int *criarVetor(int tam, int isRandom){
    int *vetor = (int*)malloc(tam*sizeof(int));
    if (vetor!=NULL){
        for (int i=0; i < tam; i++){
            if (isRandom){
                int aux=(((rand() & 255)<<8 | (rand() & 255))<<8 | (rand() & 255))<<7 | (rand() & 127);
                vetor[i] = aux % 2000000001;
            }else{
                vetor[i]=-1;
            }
        }
        return vetor;
    }
}

void printVetor(int *vetor, int tam){
	for (int i=0; i < tam; i++){
		printf(" %d |", vetor[i]);
	}
	puts("\n");
}

int numeroDeDigitos(int num){
    int nDigitos=1;
    while(num>=10){
        num=num/10;
        nDigitos++;
    }
    return nDigitos;
}

int ePotencia(int num, int base){
    int aux=base;
    while(aux<num){
        aux=aux*base;
    }

    if(aux!=num){
        return 0;
    }
    return 1;
}


int metodoDivisao(int valorChave, int tamTAB){
    return valorChave % tamTAB;
}

/*int metodoDobra(int valor,int tamTab){
    int nDigitosValor = numeroDeDigitos(valor);
    int *digitos= criarVetor(nDigitosValor, 0);
    int aux = valor;
    for(int i = nDigitosValor-1; i >= 0; i--){
        digitos[i] = aux % 10;
        aux = aux / 10;
    }


    int nDigitosN = numeroDeDigitos(tamTab) - 1;
    int*dobrado = (int*)malloc(nDigitosN*sizeof(int));

    if(nDigitosValor<nDigitosN){
        return valor;
    }else{
        for(int i = 0; i+nDigitosN < nDigitosValor; i = i + nDigitosN){
            for(int j = 0; j < nDigitosN; j++){
                dobrado[j] = digitos[i+nDigitosN-j-1];
                digitos[i+nDigitosN+j] = (digitos[i+nDigitosN+j]+dobrado[j])%10;
            }
        }

    }
}*/

int metodoMultiplicacao(int tam, int valor){
    if(!(ePotencia(tam, 10))){
        exit(1);
    }

   int nDigitosTam=numeroDeDigitos(tam)-1;
   int potenciaValor=valor*1.5;
   int nDigitosPotenciaValor=numeroDeDigitos(potenciaValor);

   if(nDigitosTam >= nDigitosPotenciaValor){
        return nDigitosPotenciaValor;
   }else{
        double nDigitosRestantes=nDigitosPotenciaValor-nDigitosTam;
        return potenciaValor/(int)pow(10.0, nDigitosRestantes);
   }
}

//int metodoAnaliseDigito(){}


void executeHashs(int *n, int sizeN){
    int tamTabelas=100000;
    int *tabMetodoDivisao=criarVetor(tamTabelas, 0);
    int *tabMetodoMultiplicacao=criarVetor(tamTabelas,0);
    //int *tabMetodoDobra=criarVetor(tamTabelas, 0);
    int colisaoDivisao=executeHashComDivisao(n ,tabMetodoDivisao, sizeN, tamTabelas);
    int colisaoMultiplicacao=executeHashComMultiplicacao(n ,tabMetodoMultiplicacao, sizeN, tamTabelas);
    //printVetor(tabMetodoDivisao,tamTabelas);
    printf("Divisao\t N:%d\t Colisoes:%d**\n",sizeN, colisaoDivisao);
    printf("Multi.\t N:%d\t Colisoes:%d**\n",sizeN, colisaoMultiplicacao);
}

int executeHashComDivisao(int *n, int *tabelaHash, int sizeN, int sizeTab){
    int colisoes=0;
    for(int i=0; i<sizeN; i++){
        int chave=metodoDivisao(n[i], sizeTab);
        if(tabelaHash[chave]!=-1){
            colisoes++;
        }else if(tabelaHash[chave]==-1){
            tabelaHash[chave]=n[i];
        }
    }
    return colisoes;
}

executeHashComMultiplicacao(int *n, int *tabelaHash, int sizeN, int sizeTab){
    int colisoes=0;
    for(int i=0; i<sizeN; i++){
        int chave=metodoMultiplicacao(sizeTab,n[i]);
        if(chave<sizeTab && tabelaHash[chave]!=-1){
            colisoes++;
        }else if(chave < sizeTab && tabelaHash[chave]==-1){
            tabelaHash[chave]=n[i];
        }
    }
    return colisoes;
}
