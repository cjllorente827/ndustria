# Industrialize the process of data mining with ndustria! (WIP)

<!-- ## ToDo:
* Profiling in parallel
* When ndustria reads in "cached" information does that data automatically go to my computer's memory
    * Load memory on an as needed basis
* After using task result set task result to null and that will cause python to clear the memory 
* Config setting: Maximum file size to keep in memory  -->

# Main features 

* Simple multiprocess parallelization of arbitrary python code
* Dynamic load balancing
* Caching and reuse of intermediate data products
* Association of code and parameters with data, which updates whenever code updates
* Ease of use and understanding. Designed to work with minimal modification to existing code. 

ndustria is being built as part of a PhD dissertation and is in active development.

## Installation

Clone Repository from github and enter into the directory

```
git clone https://github.com/cjllorente827/ndustria.git
cd ndustria
```

Ppip install the package and run the set up script

```
pip install -e ".[docs]"
ndustria-init
```

The ` ".[docs]" ` implementation is optional and installs dependencies to render the documenation locally. 
Otherwise you can just use `pip install -e .`

`ndustria-init` creates a config file for ndustria and sets up your "cache" directory where the returns of your functions will be saved. If at any point you want to change your cache directory you must rerun `ndustria-init`. This script also adds a couple of things to path in your shell start up file. Therefore in order use ndustria you must reinitialize shell. If you have bash you can complete this with:

```Linux
cd
source .bashrc
```

or

```MacOS
cd
source .zshrc
```

If you use a different shell you must use whatever command corresponds to your shell. If you are also running an environment (like conda) you may need to reinitialize the enviornment after you run `source .bashrc`

Check that you can import and use ndustria

```
python 
>>> from ndustria import Pipeline
```

## How ndustria works
ndustria works by creating a `Pipeline()` or list of tasks. Each independent task should be separated into a different function and we can use the `.AddFunction()` decorator to add this task to the Pipeline. The information in the return statement will be saved to disk and can be used by other task both during this run of the script and for other runs. For Example:

```
from ndustria import Pipeline               # <-- 1. Import Pipeline from ndustria 

pipe = Pipeline()                           # <-- 2. Create a new Pipeline

@pipe.AddFunction()                         # <-- 3. Use decorator to add function to Pipeline
def filterLargeTask(path, filter_params):   # <-- 4. Function that surrounds your long-running task

    # this takes a long time to run, 
    small_subset = filterLargeDataset(path, filter_params)

    return small_subset                     #<-- 5. Save your work to disk by adding it to the return statement
```

Once you have added one or more functions to your `Pipeline()` you can use `pipe.run()` to execute your whole Pipeline. To see this in action please follow the **Tutorials**


## Building the Documenation 

To build the documentation you can run: 

```
sphinx-autobuild docs/source docs/build
``` 
