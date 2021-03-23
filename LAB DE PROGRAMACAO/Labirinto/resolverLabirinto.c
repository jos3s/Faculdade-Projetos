#include <stdio.h>
#include <stdlib.h>

int tl,tc;

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

void buscar_labirinto(int **mat,int m,int n){

    int i,j;
    char temp;
    FILE *arq = fopen("Labirinto.txt","r");
    for(i=0;i<m;i++){
        for(j=0;j<=n;j++){
            temp = fgetc(arq);
            if(temp == '+')
                mat[i][j] = 43;
            else if(temp == '-')
                mat[i][j] = 45;
            else if(temp == '¦')
                mat[i][j] = 179;
            else
                mat[i][j] = 0;
        }
    }
    fclose(arq);

}

void animacao(int **mat,int m,int n){

    int i,j;
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            if(mat[i][j]==179 ||mat[i][j]==43||mat[i][j]==45)
                printf("%c",219);
            else if(mat[i][j]==35)
                printf("%c",43);
            else if(mat[i][j]==92)
                printf("%c",248);
            else
                printf("%c",mat[i][j]);
       }
        puts("");
    }

}

void caminho_labirinto(int **mat,int m,int n){

    int i = 1,j = 1;
    mat[1][0] = 35;
    while(i != m-2 || j != n-1){
        mat[i][j] = 35;
        if(mat[i+1][j] == 0){
            i++;
        }else if(mat[i][j+1] == 0){
            j++;
        }else if(mat[i-1][j] == 0){
            i--;
        }else if(mat[i][j-1] == 0){
            j--;
        }else{
            mat[i][j] = 92;
            if(mat[i+1][j] == 35){
                i++;
            }else if(mat[i][j+1] == 35){
                j++;
            }else if(mat[i-1][j] == 35){
                i--;
            }else if(mat[i][j-1] == 35){
                j--;
            }
        }
        animacao(mat,tl,tc);
        for(int t;t<666666666;t++){

        }
        system("cls");

    }
    mat[i][j] = 35;

}

void arquivar_labirinto_resolvido(int **mat,int m,int n){

    int i,j;
    FILE *arq = fopen("Labirinto.txt","a+");
    fprintf(arq,"\n");
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

int main(){

    int m,n;
    FILE *arq = fopen("Lab_tamanho.txt","r");
    fscanf(arq,"%d %d",&m,&n);
    fclose(arq);
    tl=m;
    tc=n;
    int **mat = gerar_matriz(m,n);
    buscar_labirinto(mat,m,n);
    caminho_labirinto(mat,m,n);
    arquivar_labirinto_resolvido(mat,m,n);
    animacao(mat,m,n);
    //imprimir_matriz(mat,m,n);
    puts("Seu labirinto resolvido foi adicionado ao arquivo 'Labirinto.txt'!");
    system("pause");

return 0;
}
