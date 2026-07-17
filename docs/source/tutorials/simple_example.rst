Simple Example
==============

We can start by running: 

.. code-block:: bash
    
    python simple_example.py


We can breakdown the terminal outputs to better understand how ndustria woks. 
The first thing ndustria does is define all of the **"tasks"** in your Pipeline. 

.. code-block:: bash

    [Added Task] matrix_multiplication(N=1024)
    [Added Task] matrix_parameters(matrix_multiplication(N=1024))
    [Added Task] matrix_multiplication(N=2048)
    [Added Task] matrix_parameters(matrix_multiplication(N=2048))
    [Added Task] matrix_multiplication(N=4096)
    [Added Task] matrix_parameters(matrix_multiplication(N=4096))
    [Added Task] matrix_multiplication(N=8192)
    [Added Task] matrix_parameters(matrix_multiplication(N=8192))
    [Added Task] matrix_multiplication(N=16384)
    [Added Task] matrix_parameters(matrix_multiplication(N=16384))
    ---
    Starting a run with 10 tasks.
    ---

ndustria is able to detect which tasks depend on other tasks and will run independent tasks first and then continue onto other tasks that require the results of previous tasks. 
For example, we can see below that ndustria performs all of the :code:`matrix_multiplication` tasks first and then :code:`matrix_parameters` tasks even though this is not the order they would be executed in without ndustria.
 We can see this because ndustria saves the results to all 5 :code:`matrix_multiplication` tasks before moving onto any of the :code:`matrix_parameters` tasks. 
 This behavior is implemented for better resource utilization in parallel programs which will be discussed later. 

.. code-block:: bash

    Saved result of matrix_multiplication(N=1024) to /home/kenzerkay/.ndustria_cache/56c6f56aa673d1699f3e6a8bfe12410f
    Saved result of matrix_multiplication(N=2048) to /home/kenzerkay/.ndustria_cache/d47090ac5456be3b9d88338994375e93
    Saved result of matrix_multiplication(N=4096) to /home/kenzerkay/.ndustria_cache/48f31c91db8a3343f81b18d15f3e5ac6
    Saved result of matrix_multiplication(N=8192) to /home/kenzerkay/.ndustria_cache/4538eba62c2ed6d4bf9a01c44669bf3a
    Saved result of matrix_multiplication(N=16384) to /home/kenzerkay/.ndustria_cache/0045520ec0f36d5affa5248d172a721e
    [Rank 0] waiting on 5 Tasks
    ---
    Iteration 1 finished. 5 Tasks left
    ---

Then ndustria runs all 5 :code:`matrix_parameters` tasks and output the some simple parameters to the terminal as we ask it to do in the function. 

.. code-block:: bash

    ----------------------------------------
    Datatype of Matrix Object: <class 'numpy.ndarray'>
    Size of Matrix: (1024, 1024)
    Total Number of Elements: 1048576
    ----------------------------------------

    Saved result of matrix_parameters(matrix_multiplication(N=1024)) to /home/kenzerkay/.ndustria_cache/98f5d9aeb878357950c9975a54cf0c3d

    ----------------------------------------
    Datatype of Matrix Object: <class 'numpy.ndarray'>
    Size of Matrix: (2048, 2048)
    Total Number of Elements: 4194304
    ----------------------------------------

    Saved result of matrix_parameters(matrix_multiplication(N=2048)) to /home/kenzerkay/.ndustria_cache/a99d386c5432b7a960413e92f58b1cd3

    ----------------------------------------
    Datatype of Matrix Object: <class 'numpy.ndarray'>
    Size of Matrix: (4096, 4096)
    Total Number of Elements: 16777216
    ----------------------------------------

    Saved result of matrix_parameters(matrix_multiplication(N=4096)) to /home/kenzerkay/.ndustria_cache/77b869459b15a893a39ef61482f61702

    ----------------------------------------
    Datatype of Matrix Object: <class 'numpy.ndarray'>
    Size of Matrix: (8192, 8192)
    Total Number of Elements: 67108864
    ----------------------------------------

    Saved result of matrix_parameters(matrix_multiplication(N=8192)) to /home/kenzerkay/.ndustria_cache/4abfc0e48abadabb16d4f57974d53752

    ----------------------------------------
    Datatype of Matrix Object: <class 'numpy.ndarray'>
    Size of Matrix: (16384, 16384)
    Total Number of Elements: 268435456
    ----------------------------------------

    Saved result of matrix_parameters(matrix_multiplication(N=16384)) to /home/kenzerkay/.ndustria_cache/cb02ea6be2f7c56497cffca9c526e225
    [Rank 0] waiting on 0 Tasks
    ---
    Iteration 2 finished. 0 Tasks left
    ---


If all tasks in your program run successfully you should see the **"All done"** message at the end. 

.. code-block:: bash

    Finished all tasks after 2 iterations
    All done.


If you run :code:`python simple_example.py` again you should see 

.. code-block:: bash

    [Cache hit!] matrix_multiplication(N=1024) can be skipped
    [Cache hit!] matrix_parameters(matrix_multiplication(N=1024)) can be skipped
    [Cache hit!] matrix_multiplication(N=2048) can be skipped
    [Cache hit!] matrix_parameters(matrix_multiplication(N=2048)) can be skipped
    [Cache hit!] matrix_multiplication(N=4096) can be skipped
    [Cache hit!] matrix_parameters(matrix_multiplication(N=4096)) can be skipped
    [Cache hit!] matrix_multiplication(N=8192) can be skipped
    [Cache hit!] matrix_parameters(matrix_multiplication(N=8192)) can be skipped
    [Cache hit!] matrix_multiplication(N=16384) can be skipped
    [Cache hit!] matrix_parameters(matrix_multiplication(N=16384)) can be skipped
    ---
    Starting a run with 0 tasks.
    ---

    Finished all tasks after 0 iterations
    All done.

ndustria "recognizes" that we have run all of these tasks before and pulls the data from out :code:`ndustria_cache` directory. 
Therefore no tasks are executed when we run the script a second time. 