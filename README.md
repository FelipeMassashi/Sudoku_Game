## No que consiste este trabalho?
```bash
Nosso trabalho consiste na construção de um jogo Sudoku. O Sudoku é um jogo de raciocínio lógico que consiste
em preencher uma grade de 9x9 com números de 1 a 9, sem que haja repetições na mesma linha, coluna ou bloco de 3x3.
Tendo em vista que esse jogo possui vários graus de dificuldade e que abrange várias possibilidades de solução, iremos
criar um algoritmo, com base no algoritmo de colônia das formigas para gerar a solução mais rápida e concreta dada a dificuldade do jogo.
````

## Metodologia
```bash
Nossa metodologia para esse trabalho vai ser usar um algoritmo que implemente uma solução ainda mais rápida para Sudoku e um algoritmo
para otimizar o tempo gasto na resolução do problema de Sudoku. Para deixar o algoritmo mais rápido em sua implementação.
````

Para otimização de tempo gasto: vamos implementar a ACO, que é um algoritmo de otimização inspirado no comportamento de formigas
em busca de alimento. O algoritmo funciona da seguinte forma:

  1) Uma população de formigas é criada e cada formiga representa uma possível solução para o problema.
  2) As formigas começam a explorar o espaço de busca, colocando trilhas de feromônio nas células que visitam.
  3) As formigas são mais propensas a seguir trilhas de feromônio fortes.
  4) À medida que as formigas exploram o espaço de busca, o feromônio nas trilhas é evaporado.
  5) O algoritmo termina quando uma formiga encontra uma solução para o problema.

A ACO pode ser usada para resolver o problema de Sudoku da seguinte forma:

  1) Cada formiga representa uma possível solução para o Sudoku.
  2) As formigas começam a explorar o espaço de busca, colocando trilhas de feromônio nas células que visitam.
  3) As formigas são mais propensas a seguir trilhas de feromônio fortes.
  4) À medida que as formigas exploram o espaço de busca, o feromônio nas trilhas é evaporado.
  5) O algoritmo termina quando uma formiga encontra uma solução para o Sudoku ou quando o tempo limite é atingido.
  6) A ACO pode ser usada para resolver Sudokus mais rapidamente do que os algoritmos tradicionais de backtracking.

Isso ocorre porque a ACO explora o espaço de busca de forma mais eficiente, evitando soluções inválidas.

## Desenvolvimento e conclusões
```bash
https://docs.google.com/document/d/1BM3RbgQZxehZcj-RIZX2ESw21U9fC4AInzboPZohP5Y/edit?usp=sharing
````

## Como rodar os códigos?
```bash
  1) Clone o projeto
  2) Abra um terminal no diretório do projeto
  3) Digite "pip install -r requirements.txt"
  4) Insira "python [nome_do_arquivo.py]" para rodar
````
## Membros do grupo
```bash
Felipe Massashi (27217931) e Humberto Eduardo Ribeiro da Silva (26184672)
Institudo de ensino: Centro Universitário do Distrito Federal(UDF)
```
