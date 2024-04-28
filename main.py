import random
import numpy as np
import time


# Get indices without numpy, including check for empty list or non-numerical values
def indices(data):
    # check if list is empty
    if not data:
        return "error: list is empty"
    # check if list contains non numerical values (not int or float)
    if not all(isinstance(x, (int, float)) for x in data):
        return "error: not all elements are int or float"
    # create list of indices
    indices = list(range(len(data)))
    return indices


# Get indices with numpy, including check for empty list or non-numerical values
def indicesnp(data):
    #check if list is empty
    if not data:
        return "error: list is empty"
    # convert list to numpy array
    nparr = np.array(data)
    # check if numpy array contains non numerical values (not int or float)
    if not np.isreal(nparr).all():
        return "error: not all elements are int or float (real)"
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

print("Indices without numpy, list1")
start = time.time_ns()
ind_list1 = indices(list1)
stop = time.time_ns()
runtimeList1 = stop - start
print(ind_list1)

print("Indices without numpy, list2")
start = time.time_ns()
ind_list2 = indices(list2)
stop = time.time_ns()
runtimeList2 = stop - start
print(ind_list2)

print("Indices without numpy, list2a")
start = time.time_ns()
ind_list2a = indices(list2a)
stop = time.time_ns()
runtimeList2a = stop - start
print(ind_list2a)

print("Indices without numpy, list3")
start = time.time_ns()
ind_list3 = indices(list3)
stop = time.time_ns()
runtimeList3 = stop - start
print(ind_list3)

print("Indices WITH numpy, list1")
start = time.time_ns()
ind_listnp1 = indicesnp(list1)
stop = time.time_ns()
runtimeListnp1 = stop - start
print(ind_listnp1)

print("Indices WITH numpy, list2")
start = time.time_ns()
ind_listnp2 = indicesnp(list2)
stop = time.time_ns()
runtimeListnp2 = stop - start
print(ind_listnp2)

print("Indices WITH numpy, list2a")
start = time.time_ns()
ind_listnp2a = indicesnp(list2a)
stop = time.time_ns()
runtimeListnp2a = stop - start
print(ind_listnp2a)

print("Indices WITH numpy, list3")
start = time.time_ns()
ind_listnp3 = indicesnp(list3)
stop = time.time_ns()
runtimeListnp3 = stop - start
print(ind_listnp3)

print("\n\nRuntime Comparison")
print("1: Not using numpy, list1\n2: Using numpy, list1")
print("1: " + str(runtimeList1) + " ns or " + str(runtimeList1 / 1000000000) + " sec")
print("2: " + str(runtimeListnp1) + " ns or " + str(runtimeListnp1 / 1000000000) + " sec\n")

print("1: Not using numpy, list2\n2: Using numpy, list2")
print("1: " + str(runtimeList2) + " ns or " + str(runtimeList2 / 1000000000) + " sec")
print("2: " + str(runtimeListnp2) + " ns or " + str(runtimeListnp2 / 1000000000) + " sec\n")

print("1: Not using numpy, list2a\n2: Using numpy, list2a")
print("1: " + str(runtimeList2a) + " ns or " + str(runtimeList2a / 1000000000) + " sec")
print("2: " + str(runtimeListnp2a) + " ns or " + str(runtimeListnp2a / 1000000000) + " sec\n")

print("1: Not using numpy, list3\n2: Using numpy, list3")
print("1: " + str(runtimeList3) + " ns or " + str(runtimeList3 / 1000000000) + " sec")
print("2: " + str(runtimeListnp3) + " ns or " + str(runtimeListnp3 / 1000000000) + " sec\n")


%input("Press any key to continue")
