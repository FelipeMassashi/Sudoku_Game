## No que consiste este trabalho?
```bash
Nosso trabalho consiste na construção de um jogo Sudoku. O Sudoku é um jogo de raciocínio
lógico que consiste em preencher uma grade de 9x9 com números de 1 a 9, sem que haja
repetições na mesma linha, coluna ou bloco de 3x3. Tendo em vista que esse jogo possui vários
graus de dificuldade e que abrange várias possibilidades de solução, iremos criar um algoritmo,
com base no algoritmo de colônia das formigas para gerar a solução mais rápida e concreta dada a
dificuldade do jogo.


## Metodologia

Nossa metodologia para esse trabalho vai ser usar um algoritmo que implemente uma solução ainda
mais rápida para Sudoku e um algoritmo para otimizar o tempo gasto na resolução do problema de Sudoku.

## Para deixar o algoritmo mais rápido em sua implementação.
Usaremos o algoritmo prune() usa a técnica de pruning para resolver sudokus de forma mais rápida.
Pruning é uma técnica de poda que elimina possibilidades inválidas, reduzindo o número de possibilidades que precisam ser testadas.

No algoritmo prune(), a poda é realizada da seguinte forma:

Percorra todas as linhas e colunas do sudoku.
Para cada célula vazia, obtenha todas as possibilidades válidas para essa célula.
Se houver apenas uma possibilidade válida, atribua essa possibilidade à célula.
A poda é realizada porque, se houver apenas uma possibilidade válida para uma célula, não há necessidade de testar outras possibilidades.
Isso pode reduzir significativamente o número de possibilidades que precisam ser testadas, especialmente para sudokus difíceis.

## Para otimização de tempo gasto.
A ACO é um algoritmo de otimização inspirado no comportamento de formigas em busca de alimento. O algoritmo funciona da seguinte forma:

Uma população de formigas é criada. Cada formiga representa uma possível solução para o problema.
As formigas começam a explorar o espaço de busca, colocando trilhas de feromônio nas células que visitam.
As formigas são mais propensas a seguir trilhas de feromônio fortes.
À medida que as formigas exploram o espaço de busca, o feromônio nas trilhas é evaporado.
O algoritmo termina quando uma formiga encontra uma solução para o problema.
A ACO pode ser usada para resolver o problema de Sudoku da seguinte forma:

Cada formiga representa uma possível solução para o Sudoku.
As formigas começam a explorar o espaço de busca, colocando trilhas de feromônio nas células que visitam.
As formigas são mais propensas a seguir trilhas de feromônio fortes.
À medida que as formigas exploram o espaço de busca, o feromônio nas trilhas é evaporado.
O algoritmo termina quando uma formiga encontra uma solução para o Sudoku ou quando o tempo limite é atingido.
A ACO pode ser usada para resolver Sudokus mais rapidamente do que os algoritmos tradicionais de backtracking.
Isso ocorre porque a ACO explora o espaço de busca de forma mais eficiente, evitando soluções inválidas.
````

## Membros do grupo
```bash
Felipe Massashi e Humberto Ribeiro
```
