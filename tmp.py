#!/usr/bin/env python
##
# @package doc_example
# @brief package documentation
#
# longer description

##
# @file tmp.py
# @author Chris Sprague (email@address.com)
# @date 23 Aug 2016
# @brief Sample python file for doxygen testing

##
# @brief Foo class
#
# Longer description.
class foo():

    ##
    # @brief Sample class method; does nothing.
    # @param self reference to this class instance
    # @param x an integer; unused
    #
    # Longer description.
    def some_method(self, x):
        pass

##
#@brief Sample function. Does nothing.
#
# Longer description.
def some_function():
    pass

f = foo()
f.some_method(5)

if __name__ == '__main__':
    pass

