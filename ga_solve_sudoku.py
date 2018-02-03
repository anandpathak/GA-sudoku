'''
    Solve sudoku using Genetic Algorithm
'''
import random
import numpy as np
from generator import Generator

GENERATOR = Generator()

class GeneticSolution:
    '''
        solve sudoku using GA
    '''
    def __init__(self, sample_size):
        #hold the solution matrix
        self.solution = GENERATOR.solution_matrix()
        self.problem = GENERATOR.problem_matrix(2)
        self.position = GENERATOR.position(self.problem)
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sample_size = sample_size
        self.sample_space = np.empty((self.sample_size, len(self.position), 3), dtype=int)
    def initial_random_sample(self):
        '''
            generate initial random sample from the value array
        '''
        for i in range(self.sample_size):
            random.shuffle(self.values)
            pointer = 0
            for index, pos in enumerate(self.position):
                self.sample_space[i][index] = [pos[0], pos[1], self.values[pointer]]
                pointer = (pointer +1)%9
        return self.sample_space
    def __fitness__(self, sample_value):
        '''
            calculate number of wrong rows, column and 3x3 matrix in the sample.
        '''
        # add sample to problem matrix
        sample = np.copy(self.problem)
        for elem in sample_value:
            sample[elem[0]][elem[1]] = elem[2]
        print(sample)
        score = 27
        for i in range(9):
            if sample[i].sum() != 45:
                score = score - 1
                print("row %d  does not have proper value : %d", i, score)
            if sample[:, i].sum() != 45:
                score = score - 1
                print("col %d  does not have proper value : %d", i, score)
            sum_3x3 = 0
#            stringg = ""
            row = 3 * int(i/3)
            col = 3 * int(i%3)
            for a_row in range(row, row+3):
                for b_row in range(col, col+3):
#                    stringg = stringg + " " + str(sample[a_row][b_row]) # for debugging
                    sum_3x3 = sum_3x3 + sample[a_row][b_row]
            if sum_3x3 != 45:
                score = score -1
#                print("3x3 %d  does not have proper value : %d", i, score)
        return score
    def selection(self, samples):
        print(samples)
GS = GeneticSolution(3)
INIT_SAMPLE = GS.initial_random_sample()
print(INIT_SAMPLE)
print(GS.selection(INIT_SAMPLE))
