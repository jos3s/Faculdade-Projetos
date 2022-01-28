#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int *criarVetor(int tam);
int *duplicarVetor(int *vetor,int size);
void printVetor(int *vetor, int tam);
void printTime(char* msg,int t);

void insertionSort(int *array, int size);

void descerHeap(int *vetor, int pos, int size);
void subirHeap(int *vetor, int pos);
void buildHeap(int *vetor, int size);
int inserirNaHeap(int novoValor, int *vetor, int size);
//int *inserirNaHeap(int valor, int *vetor, int size);
int removerNaHeap(int *vetor, int size);
//int *removerNaHeap(int *vetor, int size);
void heapSort(int *vetor, int size);

void executeInsertionSort(int *vetor, int size);
void executeHeapsort(int *vetor,int size);
void executeHeapSortAndInsertionSort(int size);
void executeHeap(int addValor, int vetorSize);

int main(){
	srand(time(NULL));

	int tam=6;
	int sizes[]={1000,10000,50000,100000,500000,1000000};
    int numExe=1;

    for(int i=0;i<tam;i++){
        printf("Entrada %d:\n", sizes[i]);
        for(int j=0; j<numExe;j++){
            executeHeapSortAndInsertionSort(sizes[i]);
        }
        puts("======================================");
    }

    //ou para executar apenas o insertion sort
    //int *vetor=criarVetor(size);
    //executeInsertionSort(vetor,size);
    //ou para executar apenas o heapsort
    //int *vetor=criarVetor(size);
    //executeHeapsort(vetor, size);


    //testar uma heap, inserindo valor e removendo
    //executeHeap(56, 10);
    return 0;
}

//utilitarias
int *criarVetor(int tam){
    int *vetor = (int*)malloc(tam*sizeof(int));
    if (vetor!=NULL){
        for (int i=0; i < tam; i++){
            vetor[i] = rand()%100;
        }
        return vetor;
    }
    return NULL;
}

int *duplicarVetor(int *vetor,int size){
    int *newVetor = (int*)malloc(size*sizeof(int));
    for (int i=0; i < size; i++){
		newVetor[i] = vetor[i];
	}
	return newVetor;
}

void printVetor(int *vetor, int tam){
	for (int i=0; i < tam; i++){
		printf(" %d |", vetor[i]);
	}
	puts("\n");
}

void printTime(char* msg,int t){
    printf("Runtime %s: %lf s \n", msg, ((double)t)/((CLOCKS_PER_SEC)));
}

//insertion
void insertionSort(int *vetor, int size){
	int i, j, key;
	for(i=0; i < size; i++){
        key=vetor[i];
		j=i-1;
		while(vetor[j]>key && j>=0){
			vetor[j+1]=vetor[j];
            j--;
		}
		vetor[j+1]=key;
	}
	//return vetor;
}

//heap
void descerHeap(int *vetor, int pos, int size){
    int aux=(2*pos)+1;
    if(aux<size){
        if(aux<size-1){
            if(vetor[aux+1]>vetor[aux]){
                aux=aux+1;
            }
        }
        if(vetor[pos]<vetor[aux]){
            int save=vetor[pos];
            vetor[pos]=vetor[aux];
            vetor[aux]=save;
            descerHeap(vetor, aux, size);
        }
    }
}

void subirHeap(int *vetor, int pos){
    int p=((pos+1)/2)-1;
    if(p>=0){
        if(vetor[pos]>vetor[p]){
            int aux=vetor[pos];
            vetor[pos]=vetor[p];
            vetor[p]=aux;
            subirHeap(vetor, p);
        }
    }
}

/*int *inserirNaHeap(int novoValor, int *vetor, int size){
    int *newVetor=criarVetor(size+1);
    if(newVetor!=NULL){
        newVetor=duplicarVetor(vetor, size);
        newVetor[size]=novoValor;
        subirHeap(newVetor, size-1);
        return newVetor;
    }else{
        puts("overflow");
        return vetor;
    }
}*/

int inserirNaHeap(int novoValor, int *vetor, int size){
    if(size<=10000000){
        vetor[size]=novoValor;
        size=size+1;
        subirHeap(vetor, size-1);
        return size;
    }
    else{
        puts("overflow");
        exit(1);
    }
}

int removerNaHeap(int *vetor, int size){
    if(size!=0){
        vetor[0]=vetor[size-1];
        size=size-1;
        descerHeap(vetor,0, size);
        return size;
    }else{
        puts("underflow");
        exit(2);
    }
}

/*int *removerNaHeap(int *vetor, int size){
    int *newVetor=criarVetor(size-1);
    if(newVetor!=NULL && size!=0){
        newVetor=duplicarVetor(vetor, size-1);
        newVetor[0]=vetor[size-1];
        descerHeap(vetor, 0, size);
        return newVetor;
    }else{
        puts("underflow");
    }
}*/

void buildHeap(int *vetor, int size){
    int i;
    for(i=size/2;i>=0;i--){
        descerHeap(vetor, i, size);
    }
}

void heapSort(int *vetor, int size){
    buildHeap(vetor, size);
    int i;
    for (i=size-1; i>0;i--){
        int save=vetor[0];
        vetor[0]=vetor[i];
        vetor[i]=save;
        descerHeap(vetor,0,i);
    }
}

//executeHeapSortAndInsertionSort
void executeInsertionSort(int *vetor, int size){
    clock_t t;
    t = clock();
    insertionSort(vetor, size);
    t = clock()-t;
    printTime("Insertion Sort", t);
}

void executeHeapsort(int *vetor,int size){
    clock_t t;
    t = clock();
    heapSort(vetor, size);
    t = clock()-t;
    printTime("HeapSort", t);
}

void executeHeapSortAndInsertionSort(int size){
	int* vetor=criarVetor(size);
	int *vetorDuplicado=duplicarVetor(vetor,size);
    executeHeapsort(vetorDuplicado, size);
    executeInsertionSort(vetor, size);
}

void executeHeap(int addValor, int vetorSize){
    int realSize=10000000;
    int *vetor=criarVetor(vetorSize);
    buildHeap(vetor, vetorSize);
    puts("Heap:");
    printVetor(vetor, vetorSize);
    puts("======================================");
    printf("Inserir %d:\n", addValor);
    vetorSize=inserirNaHeap(addValor, vetor, vetorSize);
    printVetor(vetor, vetorSize);
    puts("======================================");
    puts("Removendo");
    vetorSize=removerNaHeap(vetor,vetorSize);
    printVetor(vetor,10);
    puts("======================================");
}
