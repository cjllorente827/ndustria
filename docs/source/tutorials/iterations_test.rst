ndustria Iterations
=====================

ndustria's workflow is broken up into **iterations**. 
Each iterations is based on the dependencies between the functions. 

We can see an example of how this works in :file:`iterations_test.py`. 
We see in this example that :code:`do_sum()`, :code:`do_mean()`, and :code:`do_std()` are all in the same iteration. 
All three rely on :code:`create_random_array()` which gets performed first, but :code:`do_sum()`, :code:`do_mean()`, and :code:`do_std()` are all independent and can be run in any order. 
:code:`view_data()` relys on all of these functions having been run before it occupies a 3rd iteraion after all of the other functions. 