import time
import numpy as np


# This function takes last element as pivot, places the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right
# of pivot (bottom line, sorts all elements between low and high)
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort (array, starting index, ending index)
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


try:
    input_file = sys.argv[1]
    k = sys.argv[2] #kth smallest element
    n = sys.argv[3] #read first n elements in the file

except:
input_file = "million.txt"
k = 500000
n = 1000000
r = 5

with open(input_file) as f:
    numbers = []
    for line in f: # read lines in such a way that each line is a list
        numbers.append([int(x) for x in line.split()])
    numbers = numbers[0] # there's only one line


k=48
numbers = numbers[:k]

medians = []
midpoint = int(math.floor(r/2))+1
end = k
for i in range(midpoint,end+midpoint,r):
    min = i-midpoint
    max = i+midpoint-1
    if max>k:
        max = k-1
    quickSort(numbers,min,max)


