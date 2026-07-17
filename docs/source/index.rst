.. ndustria documentation master file, created by
   sphinx-quickstart on Fri Jul 17 14:16:44 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ndustria documentation
======================

**Industrialize the process of data mining with ndustria!**

* Simple multiprocess parallelization of arbitrary python code
* Dynamic load balancing
* Caching and reuse of intermediate data products
* Association of code and parameters with data, which updates whenever code updates
* Ease of use and understanding. Designed to work with minimal modification to existing code.

ndustria is being built as part of a PhD dissertation and is in active development.


How ndustria works
-------------------

ndustria works by creating a :code:`Pipeline()` or list of tasks. 
Each independent task should be separated into a different function and we can use the :code:`.AddFunction()` decorator to add this task to the Pipeline. 
The information in the return statement will be saved to disk and can be used by other task both during this run of the script and for other runs. 
For Example:

.. code-block:: python

   from ndustria import Pipeline               # <-- 1. Import Pipeline from ndustria 

   pipe = Pipeline()                           # <-- 2. Create a new Pipeline
   
   @pipe.AddFunction()                         # <-- 3. Use decorator to add function to Pipeline
   def filterLargeTask(path, filter_params):   # <-- 4. Function that surrounds your long-running task

      # this takes a long time to run, 
      small_subset = filterLargeDataset(path, filter_params)

      return small_subset                     #<-- 5. Save your work to disk by adding it to the return statement

Once you have added one or more functions to your :code:`Pipeline()` you can use :code:`pipe.run()` to execute your whole Pipeline. 
To see this in action please follow the **Tutorials**


Site Map
--------

.. toctree::
   :maxdepth: 2

   installation
   tutorials
   shell_commands
   notes
   reference

