# Runtime comparison, insertion and merge sort
import time
import random
import matplotlib.pyplot as plt
import pandas

# number of arrays taken of each size
# time calculated from each array is averaged
number_of_arrays = 10000


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


def create_random_list_of_size(n):
    my_list = []
    for i in range(n):
        my_list.append(random.randint(1, n))
    return my_list


list_size = []
insertion_time = []
merge_time = []

for i in range(0, 200, 5):
    list_size.append(i)
    cumulative_time1 = 0
    cumulative_time2 = 0
    for j in range(0, number_of_arrays):
        random_list = create_random_list_of_size(i)
        start1 = time.time()
        sort1 = insertion_sort(random_list)
        end1 = time.time()
        cumulative_time1 = cumulative_time1 + (end1 - start1)
        start2 = time.time()
        sort2 = merge_sort(random_list)
        end2 = time.time()
        cumulative_time2 = cumulative_time2 + (end2 - start2)

    insertion_time.append(cumulative_time1 / number_of_arrays)
    merge_time.append(cumulative_time2 / number_of_arrays)

df = pandas.DataFrame({"x": list_size, "insertion_time": insertion_time, "merge_time": merge_time})
df = df[['x', 'insertion_time', 'merge_time']]
df.to_csv("report.csv")

# plotting
plt.close()
plt.tick_params(labelsize=10)
plt.plot(list_size, insertion_time, c='blue', linewidth=2, label="Insertion time")
plt.plot(list_size, merge_time, c='red', linewidth=2, label="Merge time")
plt.legend(loc='upper left', fontsize=10)
plt.xlabel('size of array', fontsize=10)
plt.ylabel('time in seconds', fontsize=10)
plt.show()
plt.savefig("img/merge_insertion_sort_comparison.png", format="png")
