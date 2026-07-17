Installation
============

Clone Repository from github and enter into the directory

.. code-block:: 

   git clone
   git clone https://github.com/cjllorente827/ndustria.git
   cd ndustria


Pip install the package and run the set up bash script


.. code-block:: 

   pip install -e .[docs]
   ndustria-init

:file:`ndustria-init` creates a config file for ndustria and sets up your "cache" directory where the returns of your functions will be saved. 
If at any point you want to change your cache directory you must rerun :file:`ndustria-init`. 
This script also adds a couple of things to path in your shell start up file. 
Therefore in order use ndustria you must reinitialize shell. 
If you have bash you can complete this with:

.. code-block:: 

   cd
   source .bashrc

If you use a different shell you must use whatever command corresponds to your shell. 
If you are also running an environment (like conda) you may need to reinitialize the enviornment after you run :code:`source .bashrc`

Check that you can import and use ndustria

.. code-block::

   python
   >>> from ndustria import Pipeline
