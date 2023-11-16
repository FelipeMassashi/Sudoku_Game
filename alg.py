import numpy as np
import time
import matplotlib.pyplot as plt

def is_valid(sudoku, x, y, value):
    return value not in sudoku[x, :] and value not in sudoku[:, y] and value not in quadrant(sudoku, x, y)


def quadrant(sudoku, x, y):
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3:(xx + 1) * 3, yy * 3:(yy + 1) * 3]


def possibilities(sudoku, x, y):
    possibilities = list()
    for value in range(1, 10):
        if is_valid(sudoku, x, y, value):
            possibilities.append(value)
    return possibilities


def medir_tempo(func, *args, **kwargs):
    tempo_inicial = time.time()
    resultado = func(*args, **kwargs)
    tempo_final = time.time()
    tempo_decorrido = tempo_final - tempo_inicial
    return resultado, tempo_decorrido


def solver(sudoku, solutions):
    for (x, y), value in np.ndenumerate(sudoku):
        if value == 0:
            for possibility in possibilities(sudoku, x, y):
                sudoku[x, y] = possibility
                solver(sudoku, solutions)
                sudoku[x, y] = 0
            return
    solutions.append(sudoku.copy())


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
    _, tempo_decorrido = medir_tempo(solver, sudoku_copia, solutions)
    
    print(f"Tempo decorrido: {tempo_decorrido:.6f} segundos")

    # Criar um gráfico
    labels = ['Tempo sem otimizacao']
    tempos = [tempo_decorrido]

    plt.bar(labels, tempos, color=['blue'])
    plt.ylabel('Tempo (segundos)')
    plt.title('Tempo para resolver o Sudoku')
    plt.show()

