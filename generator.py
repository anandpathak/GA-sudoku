'''
    Generator 9x9 sudoku matrix.
    hide some cell value from generated sudoku matrix
    check if provided matrix is same as the generated
'''
import random as random
import numpy as np
from adjacency_list import AdjacencyList

ADJACENT_LIST = AdjacencyList()
class Generator:
    '''
        generate 9x9 sudoku matrix using graph coloring method
    '''
    def __init__(self):
        self.list = ADJACENT_LIST.generate()
        self.colors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sudoku = np.zeros((9, 9))
        self.result = np.zeros((9, 9))
    def __assign_color__(self, vertex, colors, r_sudoku):
        '''
            assign a value to vertex depending on the adjacency list
        '''
        # create a local value so that on backtrack previous matrix can be used
        sudoku = np.empty_like(r_sudoku)
        sudoku[:] = r_sudoku
        # get the position in 9x9 matrix
        i = int(vertex/9)
        j = vertex % 9
        # tail case
        if vertex >= 81:
            self.result[:] = r_sudoku
            return True
        for k in range(0, 9):
            # check if coloring possible
            dicision = self.__possible_color__(vertex, colors[k], sudoku)
            #print(str(vertex)+ "("+str(i)+", "+str(j)+") color : "+ str(k)+
            #      " possible = "+str(dicision))
            if dicision:
                sudoku[i][j] = colors[k]
                test = self.__assign_color__(vertex+1, colors, sudoku)
                if test:
                    return True
                # save internal result for debugging
                #np.savetxt('zero.txt'+str(random.randrange(100, 1000)), sudoku, fmt='%d')
        return False
    def __possible_color__(self, vertex, color, sudoku):
        '''
            check if its possible to assign color to the vertex.
        '''
        for k in range(0, 80):
            if k != vertex:
                if self.list[vertex][k] == 1 and sudoku[int(k/9)][k%9] == color:
                    return False
        return True
    def solution_matrix(self):
        '''
            return the matrix with all the values
        '''
        random.shuffle(self.colors)
        self.__assign_color__(0, self.colors, self.sudoku)
        #np.savetxt('test1.txt', self.result, fmt='%d')
        return self.result
    def problem_matrix(self, remove_cells=40):
        '''
            remove X number of cells from the generated 9x9 sudoku matrix
            this function is to set the problem.
        '''
        problem = np.empty((9, 9))
        problem[:] = self.result
        position = random.sample(range(80), remove_cells)
        for elem in position:
            i = int(elem/9)
            j = int(elem % 9)
            problem[i][j] = 0
        return problem
    def position(self, problem):
        '''
            return the array of position with no value
        '''
        pos = []
        for i, row in enumerate(problem):
            for j, val in enumerate(row):
                if val == 0:
                    pos.append([i, j])
        return pos
GEN = Generator()
SOLUTION = GEN.solution_matrix()
PROBLEM = GEN.problem_matrix(5)
#np.savetxt('solution.txt', SOLUTION, fmt='%d')
#np.savetxt('problem.txt', PROBLEM, fmt='%d')

            