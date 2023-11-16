import numpy as np
import random
import time
import matplotlib.pyplot as plt
import threading

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


def aco(sudoku):
    ants = [Ant(sudoku) for _ in range(100)]
    threads = []
    for ant in ants:
        thread = threading.Thread(target=ant.move)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
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

def add_difficulty(sudoku, num_hints_to_remove):
    modified_sudoku = np.copy(sudoku)

    # Encontre as posições das dicas não nulas (valores diferentes de zero)
    filled_positions = np.transpose(np.nonzero(modified_sudoku))

    # Embaralhe as posições
    np.random.shuffle(filled_positions)

    # Remova um número específico de dicas
    for position in filled_positions[:num_hints_to_remove]:
        modified_sudoku[tuple(position)] = 0

    return modified_sudoku  

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

    
    # Número de dicas a serem removidas para adicionar dificuldade
    num_hints_to_remove = 2

    # Gere um tabuleiro com um pouco mais de dificuldade
    difficult_sudoku = add_difficulty(sudoku, num_hints_to_remove)

    solutions = list()
    solver(difficult_sudoku, solutions)

    number = 0
    for solucao in solutions:
        number = number + 1
        print(solucao)
        print("\n")


    print(f"Numero de solucoes: {number}")

    sudoku_copia = np.copy(difficult_sudoku)
    _, tempo_ant = medir_tempo(aco, sudoku_copia)
    print(f"Tempo decorrido pela otimizacao ACO: {tempo_ant:.6f} segundos")

    # Criar um gráfico
    labels = ['Tempo com otimizacao ACO']
    tempos = [tempo_ant]

    plt.bar(labels, tempos, color=['orange'])
    plt.ylabel('Tempo (segundos)')
    plt.title('Tempo para resolver o Sudoku')
    plt.show()