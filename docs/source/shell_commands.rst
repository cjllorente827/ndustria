Shell Commands
==============

ndustria has a number of shell commands that can help you access the metadata that ndustria generates with your Pipelines. 

timeit/profiling/memcheck commands
---------------------------------------

There are 3 terminal commands associated with the timeit, profiling, and memcheck Pipeline kwargs.

1) :code:`ndustria -t <name of script>` or :code:`ndustria --timeit <name of script>` will generate a graph of the wallclock time for each Task in your Pipeline.
2) :code:`ndustria -p <name of script>` or :code:`ndustria --profiling <name of script>` will show you the line by line profiling of each Task in your Pipeline.
3) :code:`ndustria -m <name of script>` or :code:`ndustria --memcheck <name of script>` will show you the line by line memory usage of each Task in your Pipeline.

You can all any of these commands with the name of your script to see the associated data, but only if the Pipeline was run with the associated kwarg set to :code:`True`.
You can see examples of these commands in the :code:`pipeline_kwargs.py` script and the associated documentation in :file:`pipeline_kwargs.rst`.

log command
-----------

:code:`ndustria -l` or :code:`ndustria --log` will show you the "log file" of your most recent Pipeline run. 
This is a condensed version of your run which will highlight ndustria's operations and any errors that migh occur during your run. 
If you run ends early due to an error you may see the message

.. code-block:: 

    [Error] Looks like the last run didn't complete any Tasks. Use "ndustria -l" to see what went wrong. Exiting.
    
prompting you to check the log file to find out more about your error. 


cache command
-------------

:code:`ndustria -c` or :code:`ndustria --cache` will show all of the cached tasks you have stored in your :code:`ndustria_cache` directory. 
This is a good way to keep track of the tasks you have run.  


delete command 
-----------------

:code:`ndustria -d <name-of-task>` or :code:`ndustria --delete_cache <name-of-task>` is a way to clear tasks from your :code:`ndustria_cache` directory.
If you have many tasks with the same name (i.e. you make many calls to the same function with different arguments) you will be asked before each iteration if you want to delete the task.

