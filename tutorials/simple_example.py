import numpy as np
from ndustria import Pipeline

pipe = Pipeline()

@pipe.AddFunction()
def matrix_multiplication(N=10):
    matrix_1 = np.random.rand(N, N)
    matrix_2 = np.random.rand(N, N)
    result_matrix = np.matmul(matrix_1, matrix_2)
    return result_matrix

@pipe.AddFunction()
def matrix_parameters(matrix):

    num_rows, num_cols = matrix.shape
    
    print("\n----------------------------------------")
    print("Datatype of Matrix Object:", type(matrix))
    print("Size of Matrix:", matrix.shape)
    print("Total Number of Elements:", num_rows*num_cols)
    print("----------------------------------------\n")

    return 
          
def main(): 

    for i in range(10, 15):
        random_arrays = matrix_multiplication(N=2**i)
        matrix_parameters(random_arrays)

    pipe.run()

main()