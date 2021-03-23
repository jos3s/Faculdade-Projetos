#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int tc,tl;

int** gerar_matriz(int m,int n){

    int i;
    int **mat = (int**)malloc(m*sizeof(int*));
    if(mat == NULL){
        puts("Sem memoria suficiente!\n");
        system("pause");
        exit(1);
    }
    for(i=0;i<m;i++){
        mat[i] = (int*)malloc(n*sizeof(int));
        if(mat[i] == NULL){
            puts("Sem memoria suficiente!\n");
            system("pause");
            exit(1);
        }
    }
    return mat;

}

void imprimir_matriz(int **mat,int m,int n){

    int i,j;
    for(i=0;i<m;i++){
        for(j=0;j<n;j++)
            printf("%c",mat[i][j]);
        puts("");
    }

}

void apagar_matriz(int **mat,int m,int n){

    int i;
    for(i=0;i<m;i++)
        free(mat[i]);
    free(mat);

}

void bordas_labirinto(int **mat,int m,int n){

    int i,j;
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            if((i%2 == 0 && j%2 == 0) && ((i == 0 || i == m-1) || (j == 0 || j == n-1)))
                mat[i][j] = 43;
            else if(i == 0 || i == m-1)
                mat[i][j] = 45;
            else if(j == 0 || j == n-1)
                mat[i][j] = 179;
            else
                mat[i][j] = 0;
        }
    }
    mat[1][0] = 0;
    mat[m-2][n-1] = 0;

}

int parede_horizontal(int **mat,int m,int n,int il,int ic){

    int i,passagem,linha = (-1);
    do{
        linha = rand()%(m-il-4)+(il+2);
    }while(linha%2 != 0 || mat[linha][ic] == 0 || mat[linha][n-1] == 0);
    for(i=ic+1;i<n-1;i++){
        if(i%2 == 0)
            mat[linha][i] = 43;
        else
            mat[linha][i] = 45;
    }
    do{
        passagem = rand()%(n-ic-2)+(ic+1);
    }while(mat[linha][passagem] == 43);
    mat[linha][passagem] = 0;
    return linha;

}

int parede_vertical(int **mat,int m,int n,int il,int ic){

    int i,passagem,coluna = (-1);
    do{
        coluna = rand()%(n-ic-4)+(ic+2);
    }while(coluna%2 != 0 || mat[il][coluna] == 0 || mat[m-1][coluna] == 0);
    for(i=il+1;i<m-1;i++){
        if(i%2 == 0)
            mat[i][coluna] = 43;
        else
            mat[i][coluna] = 179;
    }
    do{
        passagem = rand()%(m-il-2)+(il+1);
    }while(mat[passagem][coluna] == 43);
    mat[passagem][coluna] = 0;
    return coluna;

}

void gerar_labirinto(int **mat,int m,int n,int il,int ic){

    if(m-il> 4 && n-ic > 4){
        if((m-il) > (n-ic)){
            int linha = parede_horizontal(mat,m,n,il,ic);
            animacao(mat);
            for(int i=0;i<10000;i++){

            }
            system("cls");
            gerar_labirinto(mat,linha+1,n,il,ic);
            gerar_labirinto(mat,m,n,linha,ic);
        }else{
            animacao(mat);
            for(int i=0;i<10000;i++){

            }
            system("cls");
            int coluna = parede_vertical(mat,m,n,il,ic);
            gerar_labirinto(mat,m,coluna+1,il,ic);
            gerar_labirinto(mat,m,n,il,coluna);
        }
    }

}

void labirinto(int **mat,int m,int n){

    bordas_labirinto(mat,m,n);
    int linha = m/2;
    int coluna = n/2;
    if(linha%2 != 0)
        linha++;
    if(coluna%2 != 0)
        coluna++;
    int i;
    for(i=1;i<n-1;i++){
        if(i%2 == 0)
            mat[linha][i] = 43;
        else
            mat[linha][i] = 45;
    }
    for(i=1;i<m-1;i++){
        if(i%2 == 0)
            mat[i][coluna] = 43;
        else
            mat[i][coluna] = 179;
    }
            int passagem;
        do{
            passagem = rand()%(linha-1)+(1);
        }while(mat[passagem][coluna] == 43);
        mat[passagem][coluna] = 0;
        do{
            passagem = rand()%(coluna-1)+(1);
        }while(mat[linha][passagem] == 43);
        mat[linha][passagem] = 0;
        do{
            passagem = rand()%(m-linha-2)+(linha+1);
        }while(mat[passagem][coluna] == 43);
        mat[passagem][coluna] = 0;
        do{
            passagem = rand()%(n-coluna-2)+(coluna+1);
        }while(mat[linha][passagem] == 43);
        mat[linha][passagem] = 0;
        gerar_labirinto(mat,linha+1,n,0,coluna);
        gerar_labirinto(mat,linha+1,coluna+1,0,0);
        gerar_labirinto(mat,m,coluna+1,linha,0);
        gerar_labirinto(mat,m,n,linha,coluna);

}

void arquivar_labirinto(int **mat,int m,int n){

    int i,j;
    FILE *arq = fopen("Labirinto.txt","w");
    if(arq == NULL){
        puts("Ocorreu um erro envolvendo o arquivo que armazena o labirinto!\n");
        system("pause");
        exit(1);
    }
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            if(mat[i][j] == 179)
                fprintf(arq,"%c",166);
            else
                fprintf(arq,"%c",mat[i][j]);
        }
        fprintf(arq,"\n");
    }
    fclose(arq);

}

void arquivar_tamanho(int m,int n){

    FILE *arq = fopen("Lab_tamanho.txt","w");
    if(arq == NULL){
        puts("Ocorreu um erro envolvendo o arquivo que armazena o labirinto!\n");
        system("pause");
        exit(1);
    }
    fprintf(arq,"%d %d\n",m,n);
    fclose(arq);

}

void animacao(int** mat){
    int i,j;
    for(i=0;i<tl;i++){
        for(j=0;j<tc;j++){
            if(mat[i][j]==179 ||mat[i][j]==43||mat[i][j]==45)
                printf("%c",219);
            else
                printf("%c",mat[i][j]);
       }
        puts("");
    }

}

int main(){

    srand(time(NULL));
    int i,j,m,n;
    printf("Digite a quantidade de linhas da sua matriz: ");
    scanf("%d",&m);
    printf("Digite a quantidade de colunas da sua matriz: ");
    scanf("%d",&n);
    puts("");
    m = (m*2) + 1;
    n = (n*2) + 1;
    tl=m;
    tc=n;
    int **mat = gerar_matriz(m,n);
    labirinto(mat,m,n);
    animacao(mat);
    arquivar_labirinto(mat,m,n);
    arquivar_tamanho(m,n);
    printf("\nO labirinto gerado foi armazenado em um arquivo de texto chamado 'Labirinto.txt', localizado na pasta do programa.\n");
    apagar_matriz(mat,m,n);
    system("pause");

return 0;
}
