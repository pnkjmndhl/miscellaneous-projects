import numpy as np
import pandas as pd
import time
import random
import sys

# parameters fixed
r = 5

# parameters from arguments
input_file = sys.argv[1]
k = int(sys.argv[2])
n = int(sys.argv[3])


l = []
with open(input_file) as f:
    data = f.read()
    l = [int(x) for x in data.strip().split()]

l= l[:n]


# insertion sort
def insertion_sort(x):
    # for every element in our array
    if len(x) == 0 or len(x) == 1:
        return x
    for index in range(1, len(x)):
        current = x[index]
        position = index
        while position > 0 and x[position - 1] > current:
            # print("Swapped {} for {}".format(x[position], x[position-1]))
            x[position] = x[position - 1]
            # print(x)
            position -= 1
        x[position] = current
    return x


# Code for the merge sort

def merge(a, b):
    # Function to merge two arrays
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def merge_sort(x):
    # Function to sort an array using merge sort algorithm
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) / 2
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a, b)


## median of median calculation
# get_median_of_medians(l,500000)
def get_median_of_medians(big_array, k):
    n = len(big_array)
    sublist = [big_array[i:i + r] for i in range(0, n, r)]
    medians = [insertion_sort(x)[len(x) // 2] for x in sublist]
    if len(medians) <= r:
        pivot = insertion_sort(medians)[len(medians) // 2]
    else:
        pivot = get_median_of_medians(medians, len(medians) // 2)
    # partitioning step
    lows = [n for n in big_array if n < pivot]
    highs = [n for n in big_array if n > pivot]
    pivots = [n for n in big_array if n == pivot]
    # recursive
    if k < len(lows) + 1:
        return get_median_of_medians(lows, k)
    elif k < len(lows) + len(pivots) + 1:
        return pivots[0]
    else:
        return get_median_of_medians(highs, k - len(lows) - len(pivots))



print get_median_of_medians(l, k)




# comparing times
# import matplotlib.pyplot as plt
# median_time_list, merge_time_list, insertion_time_list = [], [], []
# n = 500  # for choosing sorting algorithm when n is small (200 taken)
# l=l[:n]
#
# for i in range(2, n, 20): # values of size of arrays n in each loop
#     median_times, merge_times, insert_times = [], [], []
#     for j in range(0, 100): # random pick 20 times, calculate average time
#         arr = random.sample(l, i)  # take i samples from l (for plotting time
#         t0 = time.time()
#         a = get_median_of_medians(arr, i // 2)
#         # print(a)
#         t1 = time.time()
#         # calcualte time for merge sort
#         t2 = time.time()
#         c = merge_sort(arr)
#         # print(c[i//2-1])
#         t3 = time.time()
#         t4 = time.time()
#         c = insertion_sort(arr)
#         # print(c[i//2-1])
#         t5 = time.time()
#         median_times.append((t1 - t0) * 1000)
#         merge_times.append((t3 - t2) * 1000)
#         insert_times.append((t5 - t4) * 1000)
#     median_time_list.append(sum(median_times) / len(median_times))
#     merge_time_list.append(sum(merge_times) / len(merge_times))
#     insertion_time_list.append(sum(insert_times) / len(insert_times))
#
# plt.plot(range(2, n, 20), median_time_list)
# plt.plot(range(2, n, 20), merge_time_list)
# plt.plot(range(2, n, 20), insertion_time_list)
# plt.xlabel('Array Size: ', size=12)
# plt.ylabel('Run time in (ms): ', size=12)
# plt.legend(('Median of Medians', 'Merge sort', 'Insertion sort'), loc='upper left', prop={'size': 12})
# plt.savefig("comparison.png", format="png")