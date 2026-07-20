import numpy as np
from ndustria.Pipeline import Pipeline

pipe = Pipeline(name="test_kwargs", dryrun= False, timeit = False, profiling=False, memcheck = False, parallel = False)

@pipe.AddFunction(rerun = True)
def matrix_multiplication(N=10):
    matrix_1 = np.random.rand(N, N)
    matrix_2 = np.random.rand(N, N)
    result_matrix = np.matmul(matrix_1, matrix_2)
    return result_matrix

@pipe.AddFunction(rerun = True)                     
def matrix_parameters(matrix):

    num_rows, num_cols = matrix.shape
    
    print("\n----------------------------------------")
    print("Datatype of Matrix Object:", type(matrix))
    print("Size of Matrix:", matrix.shape)
    print("Total Number of Elements:", num_rows*num_cols)
    print("----------------------------------------\n")

    return 0
          
def main(): 
    for i in range(9, 14):
        random_arrays = matrix_multiplication(N=2**i)
        matrix_parameters(random_arrays)

    pipe.run()

main()
