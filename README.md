# magiccodeloader
Dynamically load/import modules in pure python code

codeloader.py - is the main module that dynamically imports code from a file.

loadable.py, loadables/loadable.py - modules that can be imported dynamically to the load the code content

program.py - is a main application that can be run to demonstrate the actual use of codeloader.py

execution:
python program.py

tests - folder consists of unit test cases

execution:
python -m unittest tests.test_module_function_loader
or
python -m unittest tests/test_module_function_loader.py

