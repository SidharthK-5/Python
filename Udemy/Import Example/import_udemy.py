# Importing user defined module in the same folder
import recursive_function_module

help(recursive_function_module)

int_list = [100, 200, 300, 400, 500, 600, 700]
key = 400

print(recursive_function_module.binary_search(int_list, key))
