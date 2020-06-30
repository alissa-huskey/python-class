#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Short description of script"""

# The convention is to name modules (Python files) using
# lower_case_with_underscore
#
# The code for a project should be in a directory named using lowernounderscore
#   for example:
#
#   myproject/
#       my_module.py
#       my_script.py

# ### Imports ################################################################


# ## Global Variables ########################################################

# The convention is to name global variables using ALL_CAPS_WITH_UNDERSCORE
#
# GLOBAL_VARIABLE = 2


# ## Functions ###############################################################

# The convention is to name functions, arguments, and local varibales using
# lower_case_with_underscore
#

#  def some_func():
#      """Short description of the function, including info about any arguments
#         and/or return values"""
#      ...


# The main() function should be at the last function defined
#

def main():
    """The slim funcion that does the work of the script"""
    print("Well, hello.")


# ## Runner ##################################################################

# This calls the main() function if the script is being run directly
#   but not if it is being imported as a module

# This should always be at the very end of the script
#

if __name__ == "__main__":
    main()
