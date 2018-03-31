import numpy as np

class BackTrack:
    def __init__(self,problem):
        self.problem= problem
        self.position = self.get_position()
        self.iterate = 0
    def do(self):
        status = self.get_solution(0,self.problem)
        return self.problem , self.iterate

    def get_solution(self, point,matrix):
        problem = np.empty_like(matrix)
        problem[:] = matrix
        self.iterate = self.iterate+1
        if point >= len(self.position):
            self.problem = matrix 
            return True
        allowed_value = self.possible_value(point,problem)
        if len(allowed_value) == 0:
            return False
        for i in allowed_value:
            problem[self.position[point][0]][self.position[point][1]] = int(i)
            flag= self.get_solution(point+1,problem)
            if flag==True:
                return True
        return False
            

    def get_position(self):
        '''
            return the array of position with no value
        '''
        pos = []
        for i, row in enumerate(self.problem):
            for j, val in enumerate(row):
                if val == 0:
                    pos.append([i, j])
        return pos
    def possible_value(self,point,matrix):
        row = self.position[point][0]
        col = self.position[point][1]
        val = [1,2,3,4,5,6,7,8,9]

        val = list(set(val) - set (matrix[row,:]))
        val = list(set(val) - set (matrix[:,col]))
        r = 3 * int(row / 3)
        c = 3 * int(col / 3)
        val = list(set(val) - set (matrix[r:r+3,c:c+3].flatten()))
        return val
