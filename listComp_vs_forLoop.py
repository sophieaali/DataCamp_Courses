import pandas as pd
import time

# For Loop vs List Comprehension:

# List Comprehension:
list_comp_start_time = time.time()
result = [i*i for i in range(0,1000000)]
list_comp_end_time = time.time()
print("Time using the list comprehension: {} sec".format(list_comp_end_time - list_comp_start_time))

# For Loop:
for_loop_start_time = time.time()
result = []
for i in range(0,1000000):
    result.append(i*i)
for_loop_end_time = time.time()
print("Time using the for loop: {} seconds".format(for_loop_end_time - for_loop_start_time))

list_comp_time = list_comp_end_time - list_comp_start_time
for_loop_time = for_loop_end_time - for_loop_start_time
print("Difference in time: {} %".format((for_loop_time - list_comp_time)/list_comp_time*100))