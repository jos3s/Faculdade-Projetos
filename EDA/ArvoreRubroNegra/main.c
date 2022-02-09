//José Ulisses Silva Macedo Olveira - 472946
//Link:https://youtu.be/1OG4qohH2CM

//includes
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <locale.h>

//definições
#define maxNo 10000
#define maxChave 100000
#define altErro -1
#define true 1
#define false 0


//estruturas
typedef struct no *NO;

typedef struct no{
	int chave;
	char cor;
	NO dir, esq, pai;
}no;

NO externo = NULL;


//funcoes
NO alocarRN();
NO criarNovoNo(int chave);

void rotacaoEsq(NO *ptRaiz, NO x);
void rotacaoDir(NO *ptRaiz, NO x);
void corrigirInserir(NO *ptRaiz, NO z);
void inserirChaves(NO *ptRaiz, int chave);
void moverPai(NO *ptRaiz, NO u, NO v);

NO buscarNO(NO x, int chave);

void corrigirRemover(NO *ptRaiz, NO x);
NO sucessor(NO x);
void removerRN(NO *ptRaiz, NO z);
void removerChave(NO *ptRaiz, int chave);

int quantidadeDeNO(NO ptRaiz);
int verificaNO(NO ptRaiz);
int alturaNegra(NO ptRaiz);
int verificaRN(NO ptRaiz);
void infoRN(NO x);

int gerarNumeroAleatorio();

void desaloca(NO ptRaiz);

int main(){
    setlocale(LC_ALL, "Portuguese");
    srand(time(NULL));

    int numeroRN = 0;
    int numeroRNParaTeste=1;
    int numeroDeNO = 0;
    int numeroDeNoParaTeste=100;
    int numeroDeNoRemoverParaTeste=10;
    int chaveGerada = 0;
    NO elementosExistente = NULL;
    NO ptRaiz = alocarRN();

    while(numeroRN < numeroRNParaTeste) {
        printf("\n");
        printf("\n ------- Árvore %d ------- ", 1+numeroRN);
        numeroDeNO = 0;

        while(numeroDeNO < numeroDeNoParaTeste) {
            chaveGerada = gerarNumeroAleatorio();
            if(buscarNO(ptRaiz, chaveGerada)->chave == 0) {
                inserirChaves(&ptRaiz, chaveGerada);
                numeroDeNO++;
            }
        }
        infoRN(ptRaiz);

        while(numeroDeNO > (numeroDeNoParaTeste - numeroDeNoRemoverParaTeste)) {
            removerChave(&ptRaiz, ptRaiz->chave);
            numeroDeNO--;
        }

        printf("\n");
        infoRN(ptRaiz);
        numeroRN++;
        desaloca(ptRaiz);
        ptRaiz = externo;
    }

}


int gerarNumeroAleatorio () {
  return (rand()%maxChave)+1;
}

NO alocarRN() {
    if(externo == NULL){
        externo = (NO) malloc(sizeof(struct no));
        externo->cor = 'N';
        externo->dir = externo;
        externo->esq = externo;
        externo->pai = externo;
        externo->chave = 0;
    }
    return externo;
}

NO criarNovoNo(int chave) {
    NO novo = (NO) malloc(sizeof(struct no));
    novo->chave = chave;
    novo->cor = 'R';
    novo->dir = externo;
    novo->esq = externo;
    novo->pai = externo;
    return novo;
}


void rotacaoEsq (NO *ptRaiz, NO x) {
    NO y;
    y = x->dir;
    x->dir = y->esq;

    if (y->esq != externo){
        y->esq->pai = x;
    }

    y->pai = x->pai;

    if (x->pai == externo) {
        (*ptRaiz) = y;
    } else if (x == x->pai->esq) {
        x->pai->esq = y;
    }else{
        x->pai->dir = y;
    }

    y->esq = x;
    x->pai = y;
}

void rotacaoDir (NO *ptRaiz, NO x) {
    NO y;
    y = x->esq;
    x->esq = y->dir;

    if (y->dir != externo) {
        y->dir->pai = x;
    }

    y->pai = x->pai;

    if (x->pai == externo) {
        (*ptRaiz) = y;
    } else if (x == x->pai->dir) {
        x->pai->dir = y;
    } else {
        x->pai->esq = y;
    }

    y->dir = x;
    x->pai = y;
}

void inserirChaves(NO *ptRaiz, int chave){
    NO y, x, z;
    z = criarNovoNo(chave);
    y = externo;
    x = *ptRaiz;

    while(x != externo){
        y = x;

        if(z->chave == x->chave){
            return;
        }

        if(z->chave < x->chave){
        x = x->esq;
        } else {
        x = x->dir;
        }
    }

    z->pai = y;
    if(y == externo){
        *ptRaiz = z;
    }else if(z->chave < y->chave){
        y->esq = z;
    }else{
        y->dir = z;
    }

    z->esq = externo;
    z->dir = externo;
    z->cor = 'R';

    corrigirInserir(ptRaiz, z);
    //return 0;
}

void corrigirInserir (NO *ptRaiz, NO z) {
    NO y;
    while (z->pai->cor == 'R') {

        if(z->pai == z->pai->pai->esq){
            y = z->pai->pai->dir;
            if (y->cor == 'R') {
                z->pai->cor = 'N';
                y->cor = 'N';
                z->pai->pai->cor = 'R';
                z = z->pai->pai;
            } else {
                if (z == z->pai->dir) {
                    z = z->pai;
                    rotacaoEsq(ptRaiz, z);
                }
                z->pai->cor = 'N';
                z->pai->pai->cor = 'R';
                rotacaoDir(ptRaiz, z->pai->pai);
            }
        }else{
            y = z->pai->pai->esq;
            if (y->cor == 'R') {
                z->pai->cor = 'N';
                y->cor = 'N';
                z->pai->pai->cor = 'R';
                z = z->pai->pai;
            } else {
                if (z == z->pai->esq) {
                    z = z->pai;
                    rotacaoDir(ptRaiz, z);
                }
                z->pai->cor = 'N';
                z->pai->pai->cor = 'R';
                rotacaoEsq(ptRaiz, z->pai->pai);
            }
        }
    }
    (*ptRaiz)->cor = 'N';
}

void moverPai (NO *ptRaiz, NO u, NO v) {
    if (u->pai == externo) {
        (*ptRaiz) = v;
    } else if (u==u->pai->esq) {
        u->pai->esq = v;
    } else {
        u->pai->dir = v;
    }
    v->pai = u->pai;
}

NO buscarNO (NO x, int chave) {
    if(x == externo || x->chave == chave){
        return x;
    }

    if(chave < x->chave){
        buscarNO(x->esq, chave);
    }else{
        buscarNO(x->dir, chave);
    }
}

void corrigirRemover (NO *ptRaiz, NO x) {
    NO w;

    while(x!=(*ptRaiz) && x->cor == 'N') {
        if(x == x->pai->esq) {
            w = x->pai->dir;
            if(w->cor == 'R'){
                w->cor = 'N';
                x->pai->cor = 'R';
                rotacaoEsq(ptRaiz, x->pai);
                w = x->pai->dir;
            }
            if (w->esq->cor == 'N' && w->dir->cor=='N'){
                w->cor = 'R';
                x= x->pai;
            }else{
                if(w->dir->cor == 'N') {
                    w->esq->cor =  'N';
                    w->cor = 'R';
                    rotacaoDir(ptRaiz, w);
                    w = x->pai->dir;
                }
                w->cor = x->pai->cor;
                x->pai->cor = 'N';
                w->dir->cor = 'N';
                rotacaoEsq(ptRaiz, x->pai);
                x = *ptRaiz;
            }
        }else{
            w = x->pai->esq;
            if (w->cor == 'R') {
                w->cor = 'N';
                x->pai->cor = 'R';
                rotacaoDir(ptRaiz, x->pai);
                w = x->pai->esq;
            }

            if ((w->dir->cor == 'N') && (w->esq->cor == 'N')) {
                w->cor = 'R';
                x = x->pai;
            } else {
                if (w->esq->cor == 'N') {
                    w->dir->cor = 'N';
                    w->cor = 'R';
                    rotacaoEsq(ptRaiz, w);
                    w = x->pai->esq;
                }
                w->cor = x->pai->cor;
                x->pai->cor = 'N';
                w->esq->cor = 'N';
                rotacaoDir(ptRaiz, x->pai);
                x = *ptRaiz;
            }
        }
    }
    x->cor = 'N';
}

NO sucessor (NO x) {
    NO y = x;
    while (y->esq != externo) {
        y = y->esq;
    }
    return y;
}

void removerRN (NO *ptRaiz, NO z) {
    NO y = z;
    NO x;
    char corOriginal = y->cor;

    if(z->esq == externo){
        x = z->dir;
        moverPai(ptRaiz, z, z->dir);
    }else if(z->dir == externo){
        x = z->esq;
        moverPai(ptRaiz, z, z->esq);
    }else{
        y = sucessor(z->dir);
        corOriginal = y->cor;
        x= y->dir;

        if (y->pai == z) {
            x->pai = y;
        }else{
            moverPai(ptRaiz, y, y->dir);
            y->dir = z->dir;
            y->dir->pai = y;
        }

        moverPai(ptRaiz, z, y);
        y->esq = z->esq;
        y->esq->pai = y;
    }

    if (corOriginal == 'N') {
        corrigirRemover(ptRaiz, x);
    }

    (*ptRaiz)->cor = 'N';
}

void removerChave (NO *ptRaiz, int chave) {
    NO z = buscarNO(*ptRaiz, chave);
    NO aux = z;
    if (z == externo){
        return;
    }else{
        removerRN(ptRaiz, z);
    }
    free(aux);
}

int quantidadeDeNO (NO ptRaiz) {
    if(ptRaiz == externo){
        return 0;
    }

    return 1 + quantidadeDeNO(ptRaiz->esq) + quantidadeDeNO(ptRaiz->dir);
}

int verificaNO (NO ptRaiz) {
    int analisaDir, analisaEsq;

    if(ptRaiz == externo){
        return true;
    }

    if(ptRaiz->cor == 'R'){
        if((ptRaiz->dir->cor == 'N') && (ptRaiz->esq->cor == 'N')) {
            analisaDir = verificaNO(ptRaiz->dir);
            analisaEsq = verificaNO(ptRaiz->esq);
            if (analisaDir == false || analisaEsq == false){
                return false;
            }else{
                return true;
            }
        }else{
            return false;
        }
    }else{
        analisaDir = verificaNO(ptRaiz->dir);
        analisaEsq = verificaNO(ptRaiz->esq);
        if(analisaDir == false || analisaEsq == false){
            return false;
        }else{
            return true;
        }
    }
}

int alturaNegra (NO ptRaiz) {
    if(ptRaiz == externo){
        return 1;
    }

    int altEsq = alturaNegra(ptRaiz->esq);
    int altDir = alturaNegra(ptRaiz->dir);

    if(altEsq != altDir){
        return altErro;
    }

    if(ptRaiz->cor == 'N'){
        if(altDir > altEsq){
            return 1 + altDir;
        }else{
            return 1 + altEsq;
        }
    } else {
        if(altDir > altEsq){
            return altDir;
        }else{
          return altEsq;
        }
    }
}

int verificaRN(NO ptRaiz){
    NO aux = ptRaiz;

    if(aux->cor == 'R'){
        return false;
    }

    int analisaEsq = verificaNO(aux->esq);
    int analisaDir = verificaNO(aux->dir);
    int altEsq = alturaNegra(aux->esq);
    int altDir = alturaNegra(aux->dir);

    if((altEsq != altDir) || (altDir == altErro) || (altEsq == altErro)){
        return false;
    }
    if(analisaDir == false || analisaEsq == false){
        return false;
    }else{
        return true;
    }
}

void infoRN (NO x) {
    if(verificaRN(x) == true) {
        printf("\nÉ Rubro Negra!");
    }else{
        printf("\nNão é Rubro Negra!");
    }
    printf("\nNúmero de nos: %d",quantidadeDeNO(x));
}

void desaloca (NO ptRaiz) {
    if (ptRaiz != externo) {
        desaloca(ptRaiz->dir);
        desaloca(ptRaiz->esq);
        free(ptRaiz);
    }
}

