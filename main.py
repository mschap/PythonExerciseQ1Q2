import random
import numpy as np
import time

# Define a custom exception class
class myErrorMsg(Exception):
    pass

# Get indices without numpy, including check for empty list or non-numerical values
def indices(data):
    # check if list is empty
    if not data:
        raise myErrorMsg("list is empty")
    # check if list contains non numerical values (not int or float)
    if not all(isinstance(x, (int, float)) for x in data):
        raise myErrorMsg("not all elements are int or float")
    # create list of indices
    indices = list(range(len(data)))
    return indices


# Get indices with numpy, including check for empty list or non-numerical values
def indicesnp(data):
    #check if list is empty
    if not data:
        raise myErrorMsg("list is empty")
    # convert list to numpy array
    nparr = np.array(data)
    # check if numpy array contains non numerical values (not int or float)
    if not np.isreal(nparr).all():
        raise myErrorMsg("not all elements are int or float (real)")
    # create list of indices with numpy
    indices = np.arange(len(data))
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
    ind_list1 = indices(list1)
    stop = time.time_ns()
    runtimeList1 = stop - start
    print(ind_list1)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices without numpy, list2")
try:
    start = time.time_ns()
    ind_list2 = indices(list2)
    stop = time.time_ns()
    runtimeList2 = stop - start
    print(ind_list2)
except myErrorMsg as e:
    print("MyError: " + str(e))


print("\nIndices without numpy, list2a")
try:
    start = time.time_ns()
    ind_list2a = indices(list2a)
    stop = time.time_ns()
    runtimeList2a = stop - start
    print(ind_list2a)
except myErrorMsg as e:
    print("MyError: " + str(e))

input("\nPress any button to continue...")

print("\nIndices without numpy, list3")
try:
    start = time.time_ns()
    ind_list3 = indices(list3)
    stop = time.time_ns()
    runtimeList3 = stop - start
    print(ind_list3)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list1")
try:
    start = time.time_ns()
    ind_listnp1 = indicesnp(list1)
    stop = time.time_ns()
    runtimeListnp1 = stop - start
    print(ind_listnp1)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list2")
try:
    start = time.time_ns()
    ind_listnp2 = indicesnp(list2)
    stop = time.time_ns()
    runtimeListnp2 = stop - start
    print(ind_listnp2)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list2a")
try:
    start = time.time_ns()
    ind_listnp2a = indicesnp(list2a)
    stop = time.time_ns()
    runtimeListnp2a = stop - start
    print(ind_listnp2a)
except myErrorMsg as e:
    print("MyError: " + str(e))

print("\nIndices WITH numpy, list3")
try:
    start = time.time_ns()
    ind_listnp3 = indicesnp(list3)
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
