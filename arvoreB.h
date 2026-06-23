#ifndef ARVOREB_H
#define ARVOREB_H

#define P 3          // ordem interno (p)
#define PFOLHA 2     // ordem folha (pfolha)



typedef struct No {
    int folha;
    int n;

    int chaves[P];
    struct No* filhos[P + 1];

    struct No* prox;
} No;

typedef struct {
    int promoveu;
    int chavePromovida;
    No* novoNo;
} Resultado;

typedef struct {
    int underflow;   // 1 se ficou abaixo do mínimo
} ResultadoRemocao;



No* criarNo(int folha);
int encontrarPosicao(No* no, int chave);
//determinar qual ponteiro filho seguir
//Usada na busca e na inserção

No* buscarFolha(No* raiz, int chave);
//Percorre a árvore para encontrar a folha onde a chave deve ser inserida
//Base para a inserção

int buscar(No* raiz, int chave);
//Verifica se a chave existe na árvore, retornando 1 se encontrada e 0 caso contrário
//Usada para validar a inserção e para consultas

Resultado inserirEmFolha(No* folha, int chave);
//Insere a chave na folha, mantendo as chaves ordenadas
//Se a folha ficar cheia, divide a folha e promove a chave do meio para o pai
//Retorna um resultado indicando se houve promoção, a chave promovida e o novo nó criado (se houver)

Resultado inserirRec(No* no, int chave);
//Função recursiva de inserção
//Se o nó for folha, insere diretamente
//Se for interno, chama recursivamente no filho correto e depois trata a promoção se necessário

Resultado inserirEmInterno(No* no, int chave, No* novoFilho);
//Insere a chave em um nó interno, mantendo as chaves ordenadas
//Se o nó interno ficar cheio, divide o nó e promove a chave do meio para o pai
//Retorna um resultado indicando se houve promoção, a chave promovida e o novo nó criado (se houver)

No* inserir(No* raiz, int chave);
//Função principal de inserção

int validarArvore(No* raiz);

int validarArvoreRec(No* no, int ehRaiz);

void buscarIntervalo(No* raiz, int inicio, int fim);


int removerDaFolha(No* folha, int chave);

ResultadoRemocao removerRec(No* no, int chave);

int corrigirUnderflow(No* pai, int indiceFilho);

void remover(No** raiz, int chave);

void imprimirArvore(No* raiz);

//Função para imprimir a árvore (para fins de depuração)

#endif