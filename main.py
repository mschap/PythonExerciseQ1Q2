import random
import numpy as np
import time

# Define a custom exception class
class myErrorMsg(Exception):
    pass

# Get indices without numpy, including check for empty list or non-numerical values
def indices_new(values):
    # check if list is empty
    if not values:
        raise myErrorMsg("list is empty")
    # check if list contains non numerical values (not int or float)
    if not all(isinstance(x, (int, float)) for x in values):
        raise myErrorMsg("not all elements are int or float")
    # create keys/indices
    keys = list(range(len(values)))
    # build a dictionary
    d = {}
    for i in range(len(keys)):
        d.update({keys[i]: values[i]})
    # sort dictionary by value
    sorted_by_val = dict(sorted(d.items(), key=lambda x: x[1]))
    # extract indices (dict keys) as list
    indices = list(sorted_by_val.keys())
    return indices

# Get indices with numpy, including check for empty list or non-numerical values
def indicesnp_new(data):
    #check if list is empty
    if not data:
        raise myErrorMsg("list is empty")
    # convert list to numpy array
    values = np.array(data)
    # check if numpy array contains non numerical values (not int or float)
    if not np.isreal(values).all():
        raise myErrorMsg("not all elements are int or float (real)")
    # get keys
    keys = np.arange(len(values))
    key_value_pairs = np.array([(key, value) for key, value in zip(keys, values)],
                               dtype=[('key', 'U1'), ('value', float)])
    sorted_array = np.sort(key_value_pairs, order='value')
    indices = []
    for i in sorted_array:
        indices.append(i[0])
    return indices

list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
list2a = [20, 50, 70, "abc", 8]
list3 = []

# create content of list3. 1 million random int values
for i in range(0, 1000000):
    list3.append(random.randint(0, 1000))

print("\nIndices without numpy, list1")
try:
    start = time.time_ns()
    ind_list1 = indices_new(list1)
    stop = time.time_ns()
    runtimeList1 = stop - start
    print(ind_list1)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices without numpy, list2")
try:
    start = time.time_ns()
    ind_list2 = indices_new(list2)
    stop = time.time_ns()
    runtimeList2 = stop - start
    print(ind_list2)
except myErrorMsg as e:
    print("MyError: " + str(e))


print("\nIndices without numpy, list2a")
try:
    start = time.time_ns()
    ind_list2a = indices_new(list2a)
    stop = time.time_ns()
    runtimeList2a = stop - start
    print(ind_list2a)
except myErrorMsg as e:
    print("MyError: " + str(e))

input("\nPress any button to continue...")

print("\nIndices without numpy, list3")
try:
    start = time.time_ns()
    ind_list3 = indices_new(list3)
    stop = time.time_ns()
    runtimeList3 = stop - start
    print(ind_list3)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list1")
try:
    start = time.time_ns()
    ind_listnp1 = indicesnp_new(list1)
    stop = time.time_ns()
    runtimeListnp1 = stop - start
    print(ind_listnp1)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list2")
try:
    start = time.time_ns()
    ind_listnp2 = indicesnp_new(list2)
    stop = time.time_ns()
    runtimeListnp2 = stop - start
    print(ind_listnp2)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list2a")
try:
    start = time.time_ns()
    ind_listnp2a = indicesnp_new(list2a)
    stop = time.time_ns()
    runtimeListnp2a = stop - start
    print(ind_listnp2a)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list3")
try:
    start = time.time_ns()
    ind_listnp3 = indicesnp_new(list3)
    stop = time.time_ns()
    runtimeListnp3 = stop - start
    print(ind_listnp3)
except myErrorMsg as e:
    print("MyError: " + str(e))


# Runtime Commparison
print("\n\nRuntime Comparison")
print("1: Not using numpy, list1\n2: Using numpy, list1")
try:
    print("1: " + str(runtimeList1) + " ns or " + str(runtimeList1 / 1000000000) + " sec")
except Exception as e:
    print("Something went wrong: " + str(e))

try:
    print("2: " + str(runtimeListnp1) + " ns or " + str(runtimeListnp1 / 1000000000) + " sec\n")
except Exception as e:
    print("Something went wrong: " + str(e))



print("\n1: Not using numpy, list2\n2: Using numpy, list2")
try:
    print("1: " + str(runtimeList2) + " ns or " + str(runtimeList2 / 1000000000) + " sec")
except Exception as e:
    print("Something went wrong: " + str(e))

try:
    print("2: " + str(runtimeListnp2) + " ns or " + str(runtimeListnp2 / 1000000000) + " sec\n")
except Exception as e:
    print("Something went wrong: " + str(e))




print("\n1: Not using numpy, list2a\n2: Using numpy, list2a")
try:
    print("1: " + str(runtimeList2a) + " ns or " + str(runtimeList2a / 1000000000) + " sec")
except Exception as e:
    print("1: Something went wrong: " + str(e))

try:
    print("2: " + str(runtimeListnp2a) + " ns or " + str(runtimeListnp2a / 1000000000) + " sec\n")
except Exception as e:
    print("2: Something went wrong: " + str(e))



print("\n1: Not using numpy, list3\n2: Using numpy, list3")
try:
    print("1: " + str(runtimeList3) + " ns or " + str(runtimeList3 / 1000000000) + " sec")
except Exception as e:
    print("1: Something went wrong: " + str(e))

try:
    print("2: " + str(runtimeListnp3) + " ns or " + str(runtimeListnp3 / 1000000000) + " sec\n")
except Exception as e:
    print("2: Something went wrong: " + str(e))

# input("Press any key to continue")
