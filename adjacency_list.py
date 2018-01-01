'''
    generate adjacency matrix for 9x9 sudoku
'''
import numpy as np
class AdjacencyList:
    '''
        generated Matrix containing the connection detail for sudoku
    '''
    def __init__(self):
        self.mat = np.zeros((81, 81))
    def __vertex(self, row, column):
        '''
            convert position to vertex number. e.g 1,2,3,4...81
        '''
        return row*9 + column
    def generate(self):
        '''
            findout connections for sudoku
        '''
        for i in range(0, 9):
            for j in range(0, 9):
                vertex_number = self.__vertex(i, j)
                for k in range(0, 9):
                    self.mat[vertex_number][i*9+k] = 1
                    self.mat[vertex_number][j+k*9] = 1

                # other elements of 3x3
                #first row of 3x3
                if i%3 == 0:
                    #first col of 3x3
                    if j%3 == 0:
                        self.mat[vertex_number][vertex_number+ 10] = 1
                        self.mat[vertex_number][vertex_number+11] = 1
                        self.mat[vertex_number][vertex_number+19] = 1
                        self.mat[vertex_number][vertex_number+20] = 1
                    #2nd col of 3x3
                    if j%3 == 1:
                        self.mat[vertex_number][vertex_number+8] = 1
                        self.mat[vertex_number][vertex_number+10] = 1
                        self.mat[vertex_number][vertex_number+8+9] = 1
                        self.mat[vertex_number][vertex_number+10+9] = 1
                    #3rd col of 3x3
                    if j%3 == 2:
                        self.mat[vertex_number][vertex_number+8] = 1
                        self.mat[vertex_number][vertex_number+7] = 1
                        self.mat[vertex_number][vertex_number+8+9] = 1
                        self.mat[vertex_number][vertex_number+7+9] = 1
                #2nd row of 3x3
                if i%3 == 1:
                   #first col of 3x3
                    if j%3 == 0:
                        self.mat[vertex_number][vertex_number+10] = 1
                        self.mat[vertex_number][vertex_number+11] = 1
                        self.mat[vertex_number][vertex_number-8] = 1
                        self.mat[vertex_number][vertex_number-7] = 1
                    #2nd col of 3x3
                    if j%3 == 1:
                        self.mat[vertex_number][vertex_number+8] = 1
                        self.mat[vertex_number][vertex_number+10] = 1
                        self.mat[vertex_number][vertex_number-8] = 1
                        self.mat[vertex_number][vertex_number-10] = 1
                    #3rd col of 3x3
                    if j%3 == 2:
                        self.mat[vertex_number][vertex_number+8] = 1
                        self.mat[vertex_number][vertex_number+7] = 1
                        self.mat[vertex_number][vertex_number-10] = 1
                        self.mat[vertex_number][vertex_number-11] = 1
                #first row of 3x3
                if i%3 == 2:
                    #first col of 3x3
                    if j%3 == 0:
                        self.mat[vertex_number][vertex_number-8] = 1
                        self.mat[vertex_number][vertex_number-7] = 1
                        self.mat[vertex_number][vertex_number-8-9] = 1
                        self.mat[vertex_number][vertex_number-7-9] = 1
                    #2nd col of 3x3
                    if j%3 == 1:
                        self.mat[vertex_number][vertex_number-8] = 1
                        self.mat[vertex_number][vertex_number-10] = 1
                        self.mat[vertex_number][vertex_number-8-9] = 1
                        self.mat[vertex_number][vertex_number-10-9] = 1
                    #3rd col of 3x3
                    if j%3 == 2:
                        self.mat[vertex_number][vertex_number-10] = 1
                        self.mat[vertex_number][vertex_number-11] = 1
                        self.mat[vertex_number][vertex_number-10-9] = 1
                        self.mat[vertex_number][vertex_number-11-9] = 1
        return self.mat
# generate adjacency matrix for sudoku
#ADJACENT_LIST = AdjacencyList()
#LIST = ADJACENT_LIST.generate()
#np.savetxt('mat.txt', LIST, fmt='%d')
