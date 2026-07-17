Rerun Example
=============

:code:`rerun` is the only keyword argument for individual decorators. 
It is by default set :code:`rerun=False` as this allows us to use ndustria's main functionality of stored function returns. 
However, we can force ndustria to rerun a task whether or not we have changed the code by setting :code:`rerun=True`. 
We can see this in :code:`rerun_test.py` which is the same script as :code:`simple_example.py` but the :code:`matrix_parameters` function we have :code:`rerun=True` in the decorator. 
When we run, 

.. code-block:: bash

    python rerun_test.py

we can see the top of the output looks like 

.. code-block:: bash

    [Cache hit!] matrix_multiplication(N=1024) can be skipped
    [Added Task] matrix_parameters(matrix_multiplication(N=1024))
    [Cache hit!] matrix_multiplication(N=2048) can be skipped
    [Added Task] matrix_parameters(matrix_multiplication(N=2048))
    [Cache hit!] matrix_multiplication(N=4096) can be skipped
    [Added Task] matrix_parameters(matrix_multiplication(N=4096))
    [Cache hit!] matrix_multiplication(N=8192) can be skipped
    [Added Task] matrix_parameters(matrix_multiplication(N=8192))
    [Cache hit!] matrix_multiplication(N=16384) can be skipped
    [Added Task] matrix_parameters(matrix_multiplication(N=16384))
    ---
    Starting a run with 5 tasks.
    ---


Here ndustria runs the :code:`matrix_parameters` tasks as instructed but does not run the :code:`matrix_multiplication` tasks since we already have saved versions of these functions from when we ran :code:`simple_example.py`. 
This highlights another key component of :code:`ndustria` where it can pull cached results of a function even if the previous execution of that function was in a different script. 
