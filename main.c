#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Função p o usuário entrar com as tuplas
void inserirTuplas(char alfab[50], char estados[50], char funcao[50][50], char estInicial[3], char estsFinais[50], char alfAux[50], char simbIn[2],int *quant){
            int i = 0;
            int flag = 2;
            //Aqui o usuário entra com o alfabeto no padrão especificado
            printf("\nInsira os simbolos do Alfabeto\nATENCAO:O caracter 'Q' NAO pode ser do alfabeto pois representa os Brancos do final da palavra\n FORMATO: a,b,c\n\n");
            scanf("%s", alfab);
            fflush(stdin);
            //Aqui o usuário entra com o conjunto de esstados no padrão especificado
            printf("\nInforme o conjunto de estados possiveis \n FORMATO: q0,q1,q2\n");
            scanf("%s", estados);
            fflush(stdin);
            //Aqui entra com a quantidade de transições
            printf("Informe a quantidade de transicoes: \n");
            scanf("%d",&(*quant));
            //Aqui o usuário especifica as transições
            for(i=0; i<*quant; i++){
                printf("Informe a transicao %d\n FORMATO: q0,a,A,D,q1 (Isso equivale a (q0,a)=(q1,A,D))\n", i+1);
                scanf("%s", funcao[i]);
                fflush(stdin);
            }
            //Dentre os estados informados, o usuário especifica o estado inicial
            printf("Informe o estado inicial: \n");
            scanf("%s", estInicial);
            fflush(stdin);
            //Aqui o usuário entra com o conjunto de estados finais
            printf("Informe o conjunto de estados finais: \n");
            printf("FORMATO: q0,q1,q2\n");
            scanf("%s", estsFinais);
            fflush(stdin);
            //Aqui o usuário informa se a MT tem alfabeto auxliar, se sim o usuário informa no padrão especificado
            printf("Essa MT possui alfabeto auxiliar?   1-SIM/2-NAO\n");
            scanf("%d",&flag);
            if(flag==1){
                printf("Informe o alfabeto auxiliar: \nFORMATO: a,b,c\n");
                scanf("%s",alfAux);
                fflush(stdin);
            }
            //Caso não tenha alfabeto auxiliar, essa string é NULL
            else alfAux[0] = '\0';
            //Aqui o usuário especifica o simbolo marcador de inicio
            printf("Informe o marcador de inicio (Esse marcador deve ser apenas 1 caracter DIFERENTE dos caracteres dos alfabetos)\n");
            scanf("%s",simbIn);
            fflush(stdin);
}
int EstadoAtualFazParteConjFim(char estadoAtual[3], char estsFinais[50]){
    //Essa string "aux" vai guardar o estado do conjundo de estados finais, a ser comparado com o estado atual
    char aux[3];
    int i=0;
    int j=0;
    //Aqui nós temos um for que percorre toda a string de estados finais
    for(i=0; i<strlen(estsFinais); i++){
             //Aqui verfica se o caracter da string é uma virgula, caso seja o 'j' usado na string aux é zerado,
            //para que a ariavel aux receba o estado i+1
            if(estsFinais[i]==','){
               j=0;
               continue;
            }
             //Aqui a variavel aux recebe os valores do estado a ser comparado com o estadoAtual
            aux[j] = estsFinais[i];
            j++;
            //Se j for igual a 2, é porque a aux ja foi totalmente preenchida com o estado a ser verificado
            //A strcmp compara o estado atual da MT, com o estado guardado em aux, caso sejam iguais a função retorna 1
            if(j==2){
                aux[2] = '\0';
                if(strcmp(estadoAtual,aux)==0)
                    return 1;
            }
    }
    //Se percorrer todo o for e o estado atual não estiver no conjunto de estados finais a função retorna 0
    return 0;
}
void reconhecerPalavra(char alfab[50], char estados[50], char funcao[50][50], char estInicial[3], char estsFinais[50], char alfAux[50], char simbIn[2], char simbFim[2], int *quant, char palavra[100]){
    int flag = 0;
    int flag2 = 0;
    int i=0;
    char palavraAux[100];
    palavraAux[0] = simbIn[0];
    char estadoAtual[3];
    char estadoAux[3];
    char aux2[3];
    int j=0;
    int flag3=0;
    for(i=0; i<49;i++)
        palavraAux[i] = 'Q';
        palavraAux[49] = '\0';
        palavraAux[0] = simbIn[0];
    for(i=1; i<=strlen(palavra); i++){
        palavraAux[i] = palavra[j];
        j++;
    }
    j=1;
   /* for(i=1; i<=strlen(palavra); i++){
        palavraAux[i] = palavra[i-1];
    }
    //Preenchendo o resto da string da palavra auxiliar com Q
    for(i=strlen(palavraAux); i<(48 - strlen(palavraAux)); i++){
        palavraAux[i] = 'Q';
    }
    palavraAux[49] = '\0';
    */
    //printf("\n %s \n %s \n", palavraAux, palavra);
    strcpy(estadoAtual, estInicial);
    //Sera executado enquanto o estadoCorrente n for estado final
    while(EstadoAtualFazParteConjFim(estadoAtual, estsFinais)==0){
            flag3 = 0;
            for(i=0; i<*quant; i++){
                estadoAux[0] = funcao[i][0];
                estadoAux[1] = funcao[i][1];
                estadoAux[2] = '\0';
                if(strcmp(estadoAtual, estadoAux)==0){
                        //printf("%c %c\n",palavraAux[j], funcao[i][3]);
                        if(palavraAux[j]==funcao[i][3]){
                            //printf("entrou\n%c %c\n",palavraAux[j], funcao[i][3]);
                            flag3 = 1;
                            palavraAux[j] = funcao[i][5];
                            if(funcao[i][7]=='D'){
                                j++;
                            }
                            else{
                                j--;
                            }
                            estadoAtual[0] = funcao[i][9];
                            estadoAtual[1] = funcao[i][10];
                            estadoAtual[2] = '\0';
                            if(j<0){
                                flag2 = 1;
                                break;
                            }
                            break;
                        }
                }
            }
            if(flag2==1)
                break;
            if(flag3==0)
                break;
    }
    if(flag2==1||flag3==0||(EstadoAtualFazParteConjFim(estadoAtual, estsFinais)==0)){
        printf("A palavra %s NAO e reconhecida por essa MT!\n", palavra);
    }
    else{
        if((EstadoAtualFazParteConjFim(estadoAtual, estsFinais)==1)){
            printf("A palavra %s EH reconhecida por essa MT!\n", palavra);
        }
    }
}
int main(){
    char alfab[50];
    char estados[50];
    char funcao[50][50];
    char estInicial[3];
    char estsFinais[50];
    char alfAux[50];
    char simbIn[2];
    char simbFim[2];
    int i = 0;
    int quant=0;
    char palavra[100];
    int resp=1;
    inserirTuplas (alfab, estados, funcao, estInicial, estsFinais, alfAux, simbIn,&quant);
    do{
        printf("Informe a palavra a ser reconhecida: \n");
        scanf("%s", palavra);
        fflush(stdin);
        reconhecerPalavra(alfab, estados, funcao, estInicial, estsFinais, alfAux, simbIn, simbFim, &quant, palavra);
        printf("Deseja reconhecer outra palavra usando essas mesma MT? 1-SIM / 2-NAO\n");
        scanf("%d",&resp);
    }
    while(resp==1);
    /*
    printf("alfab %s \n estados %s\n", alfab, estados);
      for(i=0; i<quant; i++){
                printf("%s\n", funcao[i]);
            }
    printf("INCIAL: %s\nFINAIS:%s\n",estInicial, estsFinais);
    printf("Auxiliar: %s\n",alfAux);
    printf("SIMBINICIAL: %s \nSIMBFIM: %s\n",simbIn, simbFim);
    */
system("pause");
return 0;
}
