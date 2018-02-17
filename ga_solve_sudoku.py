'''
    Solve sudoku using Genetic Algorithm
'''
import random
import numpy as np
from generator import Generator
GENERATOR = Generator()

class GeneticSolution:
    '''
        Identify the solution for the sudoku problem where some of the values are not provided
        in the 9x9 sudoku matrix using Genetic Algorithm
    '''
    def __init__(self, number_of_missing_values ,sample_size):
        '''
            number_of_missing_values : number of values missing in the problem sudoku
            sample_size : define the allowed number of population
        '''
        #Generate a solution matrix
        self.solution = GENERATOR.solution_matrix()
        #create the problem matrix by removing the fields
        self.problem = GENERATOR.problem_matrix(number_of_missing_values)
        #identify the missing values position
        self.position = GENERATOR.position(self.problem)
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.sample_size = sample_size
        self.number_of_missing_values = number_of_missing_values
        #create a matrix which will contain all the population solutions
        self.sample_space = np.empty((self.sample_size, len(self.position), 4))

    def firstSampleSpace(self):
        '''
            generate intial Sample space for the problem matrix
            input : none
            returns : updates the sample space and returns the sample space address
        '''
        #iterate over number of sample size
        for i in range(self.sample_size):
            #iterate over positions for each sample size
            matrix = np.copy(self.problem)
            for index, pos in enumerate(self.position):
                #find an allowed value
                self.sample_space[i][index] = [int(pos[0]), int(pos[1]), int(self.__allowedValue(pos,matrix) ), 0.0]
        return self.sample_space
    def __allowedValue(self, pos, problem):
        '''
            Calculated the values allowed at a position and return the value.
            if no value is possible to fit to the position then return a random value.
            @input : position = [x , y, value] , problem = sample conbined with  the problem matrix
            @output : the value for the position

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
            calculate number of wrong rows, column and 3x3 matrix in the sample and updating the 3rd column of position matrix .
            @input : one sample from population space
            @output : score for the sample
        '''
        # add sample to problem matrix
        sample_sudoku = np.copy(self.problem)
        #add the sample_value to problem sudoku matrix
        for elem in sample_value:
            sample_sudoku[int(elem[0])][int(elem[1])] = elem[2]
        #print("Sample Space + Problem Matrix : \n",sample_sudoku)
        score = 0
        # iterating over sample values to calculate if there are correct values in positions
        for position in sample_value:
            #Row wise checking
            if sample_sudoku[int(position[0])].sum() !=45:
                score = score +1
                position[3] = position[3] + 1
                #print("row %d  does not have proper value : %d", position, score)

            if sample_sudoku [:, int(position[1])].sum() !=45:
                score = score +1
                position[3] = position[3] + 1
                #print("col %d  does not have proper value : %d", position, score)
            sum_3x3 = 0 
            row = 3 * int(int(position[0])/3)
            col = 3 * int(int(position[1])/3)
            for a_row in range(row, row+3):
                for b_row in range(col, col+3):
#                    stringg = stringg + " " + str(sample[a_row][b_row]) # for debugging
                    sum_3x3 = sum_3x3 + sample_sudoku[a_row][b_row]
            if sum_3x3 != 45:
                score = score +1
                #print("3x3 %d  does not have proper value : %d", position, score)
                position[3] = position[3] + 1
        return score
    def fitnessCalculation(self, samples):
        '''
            @description: assign score to each position based on the correctness of the position
            @intput: population sample with positions where intput values are added
            @output: (True|False, sampleMatrix) . population sample with positions where each position assigned an score. 
                    if solution is perfect, then return true else return false.
        '''
        for sample in samples:
            score = self.__fitness__(sample)
            #print("Before:\n",sample, "\nscore:",score)
            # if score =0 means its perfect solution
            if score == 0:
                return True, sample
            for position in sample:
              position[3]= score * (position[3] +1 ) # + 1 in position to avoid 0 impact if position is right but        
        #convert score into probability
        print("before alteration\n", samples )
        for i in range(self.number_of_missing_values):
            _score = samples[:,i,3]  /  samples[:,i,3].sum()
            for y, value in enumerate(_score):
                samples[y,i,3] = value
            print(samples[:,1,3])
            
        return False,samples
    def populationGenerate(self, samples): 
        '''
            generate new sample space from fittest samples
        '''
        for sample in samples:
            for i in range(self.number_of_missing_values):
                probabilities = np.array(samples[:,i,3])
                probabilities  /= probabilities.sum() 
                sample[i,2] = np.random.choice(samples[:,i,2], p = probabilities)
                sample[i,3] = 0 
        return samples

GS = GeneticSolution(15,2)
INIT_SAMPLE = GS.firstSampleSpace()
print("Initial Sample space\n", INIT_SAMPLE)
for i in range(5000):
    SOLUTION, CALCULATED_SAMPLE = GS.fitnessCalculation(INIT_SAMPLE)
    if SOLUTION == True:
        print ("iteration : ", i," \nsolution:, \n",CALCULATED_SAMPLE)
        exit()
    else:
        print("calculated sample\n", CALCULATED_SAMPLE)
        NEW_SAMPLE = GS.populationGenerate(CALCULATED_SAMPLE)
        print("iteration ", i ," \nNEW_SAMPLE\n", NEW_SAMPLE)
        INIT_SAMPLE= NEW_SAMPLE
        

