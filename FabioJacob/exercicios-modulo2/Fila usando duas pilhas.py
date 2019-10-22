"""
Fila usando duas pilhas

Uma fila é um tipo de dados abstrato que mantém a ordem na qual os elementos foram adicionados 
a ela, permitindo que os elementos mais antigos sejam removidos da frente e os novos elementos 
sejam adicionados na parte traseira. Isso é chamado de estrutura de dados FIFO ( First-In-First
-Out ), porque o primeiro elemento adicionado à fila (ou seja, o que está esperando há mais tem-
po) é sempre o primeiro a ser removido.

Uma fila básica possui as seguintes operações:

Enfileirar : adicione um novo elemento ao final da fila.
Retirar da fila : remova o elemento da frente da fila e retorne-o.
Neste desafio, você deve primeiro implementar uma fila usando duas pilhas. Em seguida, processe 
'q' consultas, em que cada consulta é um dos seguintes 3 tipos:

    1. 1 x: Enfileire o elemento 'x' no final da fila.
    2. 2: Desenfileire o elemento na frente da fila.
    3. 3: Imprima o elemento na frente da fila.

Formato de entrada:
===================

A primeira linha contém um único número inteiro 'q', denotando o número de consultas.
Cada linha 'i' das 'q' linhas subseqüentes contém uma única consulta no formulário descrito na declaração do problema acima. Todas
as três consultas começam com um número inteiro que indica a consulta , mas apenas a consulta é seguida por um valor adicional
separado por espaço , indicando o valor a ser enfileirado. 'type1x'


Restrições:
===========

- 1 <= q <= 10⁵
- 1 <= type <= 3
- 1 <= |x| <= 10⁹

É garantido que sempre existe uma resposta válida para cada consulta do tipo 3.

Formato de saída:
=================

Para cada consulta do tipo 3, imprima o valor do elemento na frente da fila em uma nova linha.

Entrada de amostra:
===================


10
1 42
21
14
31
28
31
60
1 78
22

Saída de amostra:
=================

14
14

Explicação:
===========

Realizamos a seguinte sequência de ações:
1. Enfileirar ; .42queued = {42}
2. Retirar a fila do valor no início da fila ; .42queued = {}
3. Enfileirar ; .14queued = {14}
4. Imprima o valor no início da fila ; .14queued = {14}
5. Enfileirar ; .28queued = {14, 28}
6. Imprima o valor no início da fila ; .14queued = {14, 28}
7. Enfileirar ; .60queued = {14, 28, 60}
8. Enfileirar ; .78queued = {14, 28, 60, 78}
9. Retirar a fila do valor no início da fila ; .14queued = {28, 60, 78}
10. Retirar a fila do valor no início da fila ; .28queued = {60, 78}
"""
