import numpy as np
import random
import time
import matplotlib.pyplot as plt

# ... (código anterior)

def is_valid(sudoku, x, y, value):
    return value not in sudoku[x, :] and value not in sudoku[:, y] and value not in quadrant(sudoku, x, y)

def quadrant(sudoku, x, y):
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3:(xx + 1) * 3, yy * 3:(yy + 1) * 3]

def possibilities(sudoku, x, y):
    possibilities = []
    for value in range(1, 10):
        if is_valid(sudoku, x, y, value):
            possibilities.append(value)
    return possibilities

def solver(sudoku, solutions):
    for (x, y), value in np.ndenumerate(sudoku):
        if value == 0:
            for possibility in possibilities(sudoku, x, y):
                sudoku[x, y] = possibility
                solver(sudoku, solutions)
                sudoku[x, y] = 0
            return
    solutions.append(sudoku.copy())

class Ant:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.solution = []

    def move(self):
        # Seleciona uma célula vazia
        row, col = self.select_cell()

        # Seleciona um dígito para a célula
        num = self.select_num(row, col)

        # Atualiza a solução
        self.sudoku[row, col] = num
        self.solution.append((row, col, num))

    def select_cell(self):
        # Seleciona uma célula vazia aleatoriamente
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.sudoku[row, col] == 0:
                return row, col

    def select_num(self, row, col):
        # Seleciona o dígito mais provável para a célula
        possibilities_list = possibilities(self.sudoku, row, col)
        if possibilities_list:
            return random.choice(possibilities_list)
        else:
            return 0

def prune(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row, col] == 0:
                possibilities_list = possibilities(sudoku, row, col)
                if len(possibilities_list) == 1:
                    sudoku[row, col] = possibilities_list[0]

def aco(sudoku):
    ants = [Ant(sudoku) for _ in range(100)]
    for _ in range(1000):
        for ant in ants:
            ant.move()
    best_ant = ants[0]
    for ant in ants:
        if ant.solution < best_ant.solution:
            best_ant = ant
    return best_ant.solution

def medir_tempo(func, *args, **kwargs):
    tempo_inicial = time.time()
    resultado = func(*args, **kwargs)
    tempo_final = time.time()
    tempo_decorrido = tempo_final - tempo_inicial
    return resultado, tempo_decorrido

if __name__ == '__main__':
    sudoku = np.array([5, 3, 0, 0, 7, 0, 0, 0, 0,
                       6, 0, 0, 1, 9, 5, 0, 0, 0,
                       0, 9, 8, 0, 0, 0, 0, 6, 0,
                       8, 0, 0, 0, 6, 0, 0, 0, 3,
                       4, 0, 0, 8, 0, 3, 0, 0, 1,
                       7, 0, 0, 0, 2, 0, 0, 0, 6,
                       0, 6, 0, 0, 0, 0, 2, 8, 0,
                       0, 0, 0, 4, 1, 9, 0, 0, 5,
                       0, 0, 0, 0, 8, 0, 0, 7, 9]).reshape([9, 9])

    solucoes = []
    solver(sudoku, solucoes)
    for solucao in solucoes:
        print(solucao)

    sudoku_copia = np.copy(sudoku)
    solucao_ant, tempo_ant = medir_tempo(aco, sudoku_copia)
    print("Solução ACO:")
    print(solucao_ant)
    print(f"Tempo decorrido pela otimização ACO: {tempo_ant:.6f} segundos")

    sudoku_copia = np.copy(sudoku)
    _, tempo_antes_poda = medir_tempo(solver, sudoku_copia, [])
    prune(sudoku_copia)
    _, tempo_depois_poda = medir_tempo(solver, sudoku_copia, [])
    print(f"Tempo decorrido antes da poda: {tempo_antes_poda:.6f} segundos")
    print(f"Tempo decorrido depois da poda: {tempo_depois_poda:.6f} segundos")

    # Criar um gráfico
    labels = ['Otimização ACO', 'Antes da Poda', 'Depois da Poda']
    tempos = [tempo_ant, tempo_antes_poda, tempo_depois_poda]

    plt.bar(labels, tempos, color=['blue', 'orange', 'green'])
    plt.ylabel('Tempo (segundos)')
    plt.title('Tempo decorrido para Otimização do Sudoku')
    plt.show()