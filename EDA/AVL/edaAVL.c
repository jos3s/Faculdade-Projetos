// Jose Ulisses S. Macedo Oliviera - 472946
// https://youtu.be/GZYtKcdjInw

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define true 1
#define false 0
#define maximo 1000000

typedef struct no {
  int chave;
  int bal;
  struct no *esq,*dir;
}NO;

void iniciarNo(NO **pt, int chave);

int numAleatorio();
int quantidadeDeNOs(NO* pt);
int altura(NO *pt);
int verificaAVL(NO* pt);
void validarAVL(NO* pt);
NO* buscar(int x, NO* pt);
void desalocar(NO *pt);

void rotacaoParaDireitarInserir(NO **pt, int *h);
void rotacaoParaEsquerdaInserir(NO **pt, int *h);
void inserir(int x, NO **pt, int *h);

void rotacaoParaDireitarRemover(NO **pt, int *h);
void rotacaoParaEsquerdaRemover(NO **pt, int *h);
void trocar(NO **x, NO **y);
void balancear(NO **pt, char r, int *h);
void remover(int x, NO **pt, int *h);

int main(int argc, char *argv[]){
    srand(time(NULL));

    int valoresGerados[100000];
    int contadorDeNOs=0;
    int valorAleatorio=0;
    int h=-2;

    int numeroDeAVLParaExecucao=1;
    int numeroDeNOSDeInsercaoParaExecucao=100;
    int numeroDeNOSDeRemocaoParaExecucao=10;
    int numeroDeNOSPosRemocao=numeroDeNOSDeInsercaoParaExecucao-numeroDeNOSDeRemocaoParaExecucao;

    for(int nAVL=0; nAVL<numeroDeAVLParaExecucao;nAVL++){
        NO* avl = NULL;
        contadorDeNOs=0;
        printf("\n===== Arvore numero %d =====\n", nAVL+1);
        while(contadorDeNOs < numeroDeNOSDeInsercaoParaExecucao){
            h = -2;
            valorAleatorio = numAleatorio();
            if (buscar(valorAleatorio, avl) == NULL) {
                valoresGerados[contadorDeNOs] = valorAleatorio;
                inserir(valorAleatorio, &avl, &h);
                contadorDeNOs++;
            }
        }

        validarAVL(avl);

        while(quantidadeDeNOs(avl) != numeroDeNOSPosRemocao && contadorDeNOs > 0){
            h = -2;
            remover(valoresGerados[--contadorDeNOs], &avl, &h);
        }

        validarAVL(avl);
        desalocar(avl);
    }

  return 0;
}


void iniciarNo(NO **pt, int chave){
    NO* novo = (NO*)malloc(sizeof(NO));
    novo->esq = NULL;
    novo->dir = NULL;
    novo->bal = 0;
    novo->chave = chave;
    (*pt) = novo;
}


int quantidadeDeNOs(NO* pt) {
  if(pt == NULL){
     return 0;
  }
  return 1 + quantidadeDeNOs(pt->esq) + quantidadeDeNOs(pt->dir);
}

int altura(NO *pt) {
  if (pt==NULL) {
   return 0;
  }

  int altEsq = altura(pt->esq);
  int altDir = altura(pt->dir);

  if (altEsq > altDir) {
    return altEsq + 1;
  } else {
    return altDir + 1;
  }
}

int verificaAVL(NO* pt){
    int validador;

    if (pt != NULL) {
        int arvEsq = verificaAVL(pt->esq);
        int arvDir = verificaAVL(pt->dir);

        if(arvEsq == false || arvDir == false){
            return false;
        }
        int calcBal = (altura(pt->dir) - altura(pt->esq));
        if (calcBal >=-1 && calcBal <=1) {
            validador = true;
        } else {
            validador = false;
        }

        return validador;
    }

    return true;
}

void validarAVL(NO* pt) {
    puts("\n");
    printf("Altura: %d\n", altura(pt));
    printf("Numero de nos: %d\n", quantidadeDeNOs(pt));
    if (verificaAVL(pt) == true) {
        printf("AVL: True!\n");
    } else {
        printf("AVL: Falso!\n");
    }
}

int numAleatorio() {
  return (rand() % maximo) + 1;
}

NO* buscar(int x, NO* pt){
    while(pt != NULL && pt->chave != x){
        if(x > pt->chave){
            pt = pt->dir;
        }else{
            pt = pt->esq;
        }
    }

    return pt;
}

void desalocar(NO *pt){
    if(pt != NULL){
        desalocar(pt->dir);
        desalocar(pt->esq);
        free(pt);
    }
}

//Caso1R
void rotacaoParaDireitarInserir(NO **pt, int *h) {
    NO *ptv = NULL;
    NO *ptu = (*pt)->esq;
    if (ptu->bal == -1) {
        (*pt)->esq = ptu->dir;
        ptu->dir = *pt;
        (*pt)->bal = 0;
        *pt = ptu;
    } else {
        ptv = ptu->dir;
        ptu->dir = ptv->esq;
        ptv->esq = ptu;
        (*pt)->esq = ptv->dir;
        ptv->dir = *pt;
        if (ptv->bal == -1) {
            (*pt)->bal = 1;
        } else {
            (*pt)->bal = 0;
        }

        if (ptv->bal == 1) {
            ptu->bal = -1;
        } else {
            ptu->bal = 0;
        }
        *pt = ptv;
   }
    (*pt)->bal = 0;
    (*h) = false;
}

//Caso2R
void rotacaoParaEsquerdaInserir(NO **pt, int *h) {
    NO *ptv = NULL;
    NO *ptu = (*pt)->dir;
    if(ptu->bal == 1) {
        (*pt)->dir = ptu->esq;
        ptu->esq = *pt;
        (*pt)->bal = 0;
        (*pt) = ptu;
    } else {
        ptv = ptu->esq;
        ptu->esq = ptv->dir;
        ptv->dir = ptu;
        (*pt)->dir = ptv->esq;
        ptv->esq = *pt;
        if (ptv->bal == 1) {
            (*pt)->bal = -1;
        } else {
            (*pt)->bal = 0;
        }
        if (ptv->bal == -1) {
            ptu->bal = 1;
        } else {
            ptu->bal = 0;
        }
        (*pt) = ptv;
    }
    (*pt)->bal =0;
    (*h) = false;
}

void inserir(int x, NO **pt, int *h) {
    if (*pt == NULL) {
        iniciarNo(pt, x);
        (*h) = true;
    } else {
        if (x == (*pt)->chave) {
            printf("\n\nElemento esta na arvore!\n");
            return;
        } else if (x < (*pt)->chave) {
            inserir(x, &(*pt)->esq, h);
            if((*h) == true) {
                switch((*pt)->bal) {
                    case 1:
                        (*pt)->bal = 0;
                        (*h) = false;
                        break;
                    case 0:
                        (*pt)->bal = -1;
                        break;
                    case -1:
                        rotacaoParaDireitarInserir(pt, h);
                        break;
                    default: printf("\n\nHouve um erro no inserir! (1)\n\n");
                }
            }
        } else {
            inserir(x, &(*pt)->dir, h);
            if((*h) == true) {
                switch((*pt)->bal){
                    case -1:
                        (*pt)->bal = 0;
                        (*h)= false;
                        break;
                    case 0:
                        (*pt)->bal = 1;
                        break;
                    case 1:
                        rotacaoParaEsquerdaInserir(pt, h);
                        break;
                    default: printf("\n\nHouve um erro no inserir! (2)\n\n");
                }
            }
        }
    }
}

//Caso1R
void rotacaoParaDireitarRemover(NO **pt, int *h){
    NO *ptu = (*pt)->esq;
    NO *ptv;
    if (ptu->bal <= 0) {
        (*pt)->esq = ptu->dir;
        ptu->dir =(*pt);
        (*pt)= ptu;
        if (ptu->bal == -1) {
            ptu->bal =(*pt)->dir->bal = 0;
            (*h) = true;
        } else {
            ptu->bal = 1;
            (*pt)->dir->bal=-1;
            (*h) = false;
        }
    } else {
        ptv = ptu->dir;
        ptu->dir = ptv->esq;
        (*pt)->esq=ptv->dir;
        ptv->esq=ptu;
        ptv->dir=(*pt);
        (*pt)=ptv;
        switch (ptv->bal) {
            case -1:
                ptu->bal = 0;
                (*pt)->dir->bal = 1;
                break;
            case 0:
                ptu->bal = (*pt)->dir->bal = 0;
                break;
            case 1:
                ptu->bal = -1;
                (*pt)->dir->bal=0;
                break;
            default:
                printf("\nHouve um erro no remover! (dir)");
            break;
        }
        (*pt)->bal = 0;
        (*h) = true;
    }
}

//Caso2R
void rotacaoParaEsquerdaRemover(NO **pt, int *h){
    NO *ptu = (*pt)->dir;
    NO *ptv;
    if (ptu->bal >= 0) {
        (*pt)->dir = ptu->esq;
        ptu->esq = (*pt);
        (*pt)= ptu;
        if (ptu->bal == 1) {
            ptu->bal=(*pt)->esq->bal = 0;
            (*h) = true;
        } else {
            ptu->bal = -1;
            (*pt)->esq->bal=1;
            (*h) = false;
        }
    } else {
        ptv = ptu->esq;
        ptu->esq = ptv->dir;
        (*pt)->dir=ptv->esq;
        ptv->dir=ptu;
        ptv->esq=(*pt);
        (*pt)=ptv;
        switch (ptv->bal) {
            case 1:
                ptu->bal = 0;
                (*pt)->esq->bal = -1;
                break;
            case 0:
                ptu->bal = (*pt)->esq->bal = 0;
                break;
            case -1:
                ptu->bal = 1;
                (*pt)->esq->bal= 0;
                break;
            default:
                printf("\nHouve um erro no remover! (esq)");
            break;
        }
        (*pt)->bal = 0;
        (*h) = true;
    }
}

void trocar(NO **x, NO **y){
    int aux = (*x)->chave;
    (*x)->chave = (*y)->chave;
    (*y)->chave = aux;
}

void balancear(NO **pt, char r, int *h)  {
    if ((*h) == true) {
        if (r == 'D') {
            switch((*pt)->bal){
                case 1:
                    (*pt)->bal = 0;
                    break;
                case 0:
                    (*pt)->bal = -1;
                    (*h) = false;
                    break;
                case -1:
                    rotacaoParaDireitarRemover(&(*pt), h);
                    break;
                default:
                    printf("\nHouve um erro no balanceamento! (1)\n");
                    break;
            }
        } else {
            switch ((*pt)->bal) {
                case -1:
                    (*pt)->bal = 0;
                    break;
                case 0:
                    (*pt)->bal = 1;
                    (*h) = false;
                    break;
                case 1:
                    rotacaoParaEsquerdaRemover(&(*pt), h);
                    break;
                default:
                    printf("\nHouve um erro no balanceamento! (2)\n");
                    break;
            }
        }
    }
}

void remover(int x, NO **pt, int *h) {
    NO** ptRaiz= pt;
    if ((*ptRaiz) == NULL) {
        printf("\nElemento (NO) inexistente\n");
        return;
    } else {
        if (x < (*ptRaiz)->chave) {
            remover(x, &(*ptRaiz)->esq, h);
            balancear(&(*ptRaiz), 'E', h);
        } else {
            if (x > (*ptRaiz)->chave) {
                remover(x, &(*ptRaiz)->dir, h);
                balancear(&(*ptRaiz), 'D', h);
            } else {
                NO *aux = (*ptRaiz);
                if ((*ptRaiz)->esq == NULL) {
                    (*ptRaiz) = (*ptRaiz)->dir;
                    (*h) = true;
                    free(aux);
                } else {
                    if ((*ptRaiz)->dir == NULL) {
                        (*ptRaiz) = (*ptRaiz)->esq;
                        (*h) = true;
                        free(aux);
                    } else {
                        NO* s = (*ptRaiz)->dir;
                        if (s->esq == NULL) {
                            (*ptRaiz)->dir = s->dir;
                            s->esq = (*ptRaiz)->esq;
                            s->bal = (*ptRaiz)->bal;
                            (*ptRaiz) = s;
                            *h = true;
                            free(aux);
                        } else {
                            NO* paiS = s;
                            while(s->esq != NULL) {
                                paiS = s;
                                s = s->esq;
                            }
                            trocar(ptRaiz, &(paiS->esq));
                            remover(x, &(*ptRaiz)->dir, h);
                        }
                        balancear(ptRaiz, 'D', h);
                    }
                }
            }
        }
    }
}


