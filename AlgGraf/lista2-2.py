#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
trabalho da lista 2
Victor Ribeiro Pires
113051532
"""

"""
exercicio 1:
o algoritmo de kruskaal resolve essa tarefa    
    enquanto  existe aresta externa a F  faça
        seja A uma aresta externa de custo minimo
        acrescente  A  a  F 
    devolva  F 
"""

"""
exercício 2:
    O algoritmo de tarjan resolve essa questão


static int pre[maxV];
static int kk;
static int low[maxV];
static Vertex stack[maxV];
static int N;
static int scnum;


int DIGRAPHscT( Digraph G) 
{
   Vertex v; 
   for (v = 0; v < G->V; v++) 
      pre[v] = -1;
   scnum = 0; N = 0; kk = 0;
   for (v = 0; v < GR->V; v++) 
      if (pre[v] == -1)
         SCdfsR( G, v);
}

void SCdfsR( Digraph G, Vertex v) 
{ 
   link a;
   pre[v] = kk++; 
   low[v] = pre[v]; 
   stack[N++] = v; 
   for (a = G->adj[v]; a != NULL; a = a->next) {
      Vertex w = a->w;
      if (pre[w] == -1) 
         SCdfsR( G, w);
      if (low[w] < low[v]) 
         low[v] = low[w];
   }
   if (low[v] < pre[v])
      return; 
   do { 
      Vertex u = stack[--N]; 
      sc[u] = scnum; 
      low[u] = G->V; 
   } while (stack[N] != v); 
   scnum++;
}

"""

"""
    exercício 3:

        O Dijkstra não é recomendado para grafos com arestas negativas.
        
        Caso execute o algoritmo, se o grafo tiver arestas negativas ele não vai retornar o menor caminho
	mas se o grafo tiver um ciclo negativo, não vai existir menor caminho.

        	Se a preocupação for rodar eternamente, não é o caso, o Dijkstra passa apenas uma vez por cada aresta.
"""

"""
    exercício 4:
	
	Começa-se pelo 2, guarda essa variavel denominador
	Enquanto o numerador da fração for diferente de 1:
		Se a fração é maior que 1 sobre denominador:
			Subtrai-se o valor da fração atual por 1/denominador
			e guarda-se 1/denominador numa lista de denominadores resultado
		denominador acrescenta mais um
	Por fim, depois do while, adiciona o ultimo fator, o valor atual da fração

	É garantido que ela retorna sempre o menor número de parcelas,
	porque se eu parti do 2 e fui aumentando, as minhas parcelas são as maiores possíveis
	É garantido que ela funciona porque ela passa por todas as parcelas possíveis

	Resta definir como trabalhar com a fração para verificar se fração é maior que 1/denominador
	Uma das soluções possiveis é com a fração e o denominador, ver
	se o numerador da fração é maior que o denominador da função dividido pelo atual denominador
	Porém a divisão dos denominadores pode não ser inteira, nesse caso, verifique se 
	eu multiplicar a função pelo denominador atual, o valor da fração é maior que 1/denominador
	se não for, simplesmente continua-se com o mesmo se for, use a nova fração
"""

"""
    exercício 5:
        #include <stdio.h>

main() {
	int Q,n1=0,n5=0,n10=0,n25=0,n50=0,n100=0;
	printf("Digite o valor: \n");
	scanf("%d",&Q);
	while(Q>0) {
		if (Q>=100) { Q=Q-100; n100=n100+1; }
		else if (Q>=50) { Q=Q-50; n50=n50+1; }
		else if (Q>=25) { Q=Q-25; n25=n25+1; }
		else if (Q>=10) { Q=Q-10; n10=n10+1; }
		else if (Q>=5) { Q=Q-5; n5=n5+1; }
		else { Q=Q-1; n1=n1+1; }
	}
	printf("%d Notas de 100, %d Notas de 50\n",n100,n50);
	printf("%d Notas de 25, %d Notas de 10\n",n25,n10);
	printf("%d Notas de 5, %d Notas de 1\n",n5,n1);
return0;
"""

"""
exercício 6:
	Dado um grafo G, e vértices U e V, origem e destino, do menor caminho
	Anote o custo para todos os vértices como sendo infinito

	Então anote o custo para o vértice U como sendo 0, marque-o
	e por fim, anote como sendo seu pai, ele mesmo

	Para todo vértice A adjacente de U:
		Anote-os como sendo seu pai, o vértice U
		e o seu respectivo custo como sendo o custo de U para A
		Coloque na lista de próximos vértices, com seu custo atual

	Para cada vértice A da lista de próximos vértices, priorizando menor custo atual:
		Se ele estiver marcado:
			Ignore a iteração
			//significa que existe aresta negativa

		Marque-o

		Se o vértice A for igual a V, o vertice destino:
			Guarde os vertices de todos os pais até U
			"Entregue" esses vertices de forma inversa //já que guardou de V->U e não U->V
			e "Entregue" o custo atual de A

		Para todo vertice B adjacente de A:
			Se B tiver pai:
				Se o custo de A para B for menor que o custo atual de B:
					Anote A como sendo pai de B
					Anotar seu custo atual como sendo o custo de A-B mais o custo de A
			Senão
				Anote A como sendo pai de B
				Anotar seu custo atual como sendo o custo de A-B mais o custo de A
				Coloque-o na lista de próximos vertices, com seu custo atual
	
	Se o código chegar nesse ponto, não existe caminho de U para V,
pode-se enviar qualquer mensagem relacionada a isso.
"""