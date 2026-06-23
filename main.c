#include <stdio.h>
#include "arvoreB.h"

int main() {

    No* raiz = NULL;

    int opcao;
    int valor;

    do {

        printf("\n=== MENU ===\n");
        printf("1 - Inserir\n");
        printf("2 - Remover\n");
        printf("3 - Imprimir\n");
        printf("4 - Validar\n");
        printf("0 - Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {

            case 1:
                printf("Valor para inserir: ");
                scanf("%d", &valor);
                raiz = inserir(raiz, valor);
                break;

            case 2:
                printf("Valor para remover: ");
                scanf("%d", &valor);
                remover(&raiz, valor);
                break;

            case 3:
                printf("\nArvore:\n");
                imprimirArvore(raiz);
                break;

            case 4:
                if (validarArvore(raiz))
                    printf("Arvore valida!\n");
                else
                    printf("Erro estrutural!\n");
                break;

            case 0:
                printf("Encerrando...\n");
                break;

            default:
                printf("Opcao invalida!\n");
        }

    } while (opcao != 0);

    return 0;
}