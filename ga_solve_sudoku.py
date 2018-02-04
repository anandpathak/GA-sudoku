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
        self.problem = GENERATOR.problem_matrix(20)
        self.position = GENERATOR.position(self.problem)
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sample_size = sample_size
        self.sample_space = np.empty((self.sample_size, len(self.position), 4), dtype=int)

    def firstSampleSpace(self):
        '''
            generate intial Sample space for the problem matrix
        '''
        #iterate over number of sample size
        for i in range(self.sample_size):
            #iterate over positions for each sample size
            matrix = np.copy(self.problem)
            for index, pos in enumerate(self.position):
                #find an allowed value
                self.sample_space[i][index] = [pos[0],pos[1], self.__allowedValue(pos,matrix), 0]
        return self.sample_space
    def __allowedValue(self, pos, problem):
        '''
            Assign random value from the list of valid values
        '''
        row = pos[0]
        col = pos[1]
        val = [1,2,3,4,5,6,7,8,9]
        # row wise check
        for i in range(9):
            try:
                val.remove(problem[row][i])
                val.remove(problem[i][col])
            except:
                pass
        row = 3 * int(pos[0] / 3)
        col = 3 * int(pos[1] / 3)
        for a_row in range(row , row+3):
            for a_col in range(col, col+3):
                try:
                    val.remove(problem[a_row][a_col])
                except:
                    pass
        if len(val) == 0:
            return random.randint(1, 9)
        else: 
            return random.choice(val)

    def __fitness__(self, sample_value):
        '''
            calculate number of wrong rows, column and 3x3 matrix in the sample.
        '''
        # add sample to problem matrix
        sample_sudoku = np.copy(self.problem)
        #add the sample_value to problem sudoku matrix
        for elem in sample_value:
            sample_sudoku[elem[0]][elem[1]] = elem[2]
        print("Sample Space + Problem Matrix : \n",sample_sudoku)
        score = 0
        # iterating over sample values to calculate if there are correct values in positions
        for position in sample_value:
            #Row wise checking
            if sample_sudoku[position[0]].sum() !=45:
                score = score +1
                position[3] = position[3] + 1
                print("row %d  does not have proper value : %d", position, score)

            if sample_sudoku [:, position[1]].sum() !=45:
                score = score +1
                position[3] = position[3] + 1
                print("col %d  does not have proper value : %d", position, score)
            sum_3x3 = 0 
            row = 3 * int(int(position[0])/3)
            col = 3 * int(int(position[1])/3)
            for a_row in range(row, row+3):
                for b_row in range(col, col+3):
#                    stringg = stringg + " " + str(sample[a_row][b_row]) # for debugging
                    sum_3x3 = sum_3x3 + sample_sudoku[a_row][b_row]
            if sum_3x3 != 45:
                score = score +1
                print("3x3 %d  does not have proper value : %d", position, score)
                position[3] = position[3] + 1
        return score
    def fitnessCalculation(self, samples):
        '''
            @description: assign score to each position based on the correctness of the position
            @intput: population sample with positions where intput values are added
            @output: population sample with positions where each position assigned an score
        '''
        for sample in samples:
            score = self.__fitness__(sample)
            print("Before:\n",sample)
            # if score =0 means its perfect solution
            if score == 0:
                return True, sample
            for position in sample:
              position[3]= score * position[3]       
        #Total Score calculation
        total_score=0
        for sample in samples:
            for position in sample:
                total_score = total_score + position[3]
        print ("Total Score", total_score)
        for sample in samples:
            for position in sample:
                try:
                    position[3] =  int(position[3]* 100 / total_score)
                except:
                    print("INFO:could be devide by zero",position,"/",total_score)
                    pass
        print ("\nafter:\n",sample)
        return False,samples
    def populationGenerate(self, samples): 
        '''
            generate new sample space from fittest samples
        '''
        for sample in samples:
        return CALCULATED_SAMPLE

GS = GeneticSolution(1)
INIT_SAMPLE = GS.firstSampleSpace()
SOLUTION, CALCULATED_SAMPLE = GS.fitnessCalculation(INIT_SAMPLE)
if SOLUTION == True:
    print ("solution:\n",CALCULATED_SAMPLE)
else:
    NEW_SAMPLE = GS.populationGenerate(CALCULATED_SAMPLE)
