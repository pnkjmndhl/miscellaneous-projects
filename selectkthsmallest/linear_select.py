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
    medians.append(midpoint[i])

quickSort(medians)


if len(medians)%2 == 0:
    median = medians[len(medians)/2]
else:
    median = medians[(len(medians)+1)/2]





# Python implementation of worst case linear time algorithm 

  
# A simple function to find median of arr[].  This is called 
# only for an array of size 5 in this program. 
def findMedian(arr, int n):
    sort(arr, arr+n);  # Sort the array
    return arr[n/2];   # Return middle element 

# Returns k'th smallest element in arr[l..r] in worst case 
# linear time. ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT 
def kthSmallest(arr, l, r, k):
     # If k is smaller than number of elements in array
    if (k > 0 & k <= r - l + 1):
        n = r-l+1 # Number of elements in arr[l..r]
          # Divide arr[] in groups of size 5, calculate median
        # of every group and store it in median[] array. 
        int i, median[(n+4)/5] # There will be floor((n+4)/5) groups;
        for i in range(0,n/5):
            median[i] = findMedian(arr+l+i*5, 5)
        if (i*5 < n): #For last group with less than 5 elements
            median[i] = findMedian(arr+l+i*5, n%5)
            i=i+1
             
  
        # Find median of all medians using recursive call. 
        # If median[] has only one element, then no need 
        # of recursive call 
        int medOfMed = (i == 1)? median[i-1]: 
                                 kthSmallest(median, 0, i-1, i/2); 
  
        # Partition the array around a random element and 
        # get position of pivot element in sorted array 
        int pos = partition(arr, l, r, medOfMed); 
  
        # If position is same as k 
        if (pos-l == k-1) 
            return arr[pos]; 
        if (pos-l > k-1)  # If position is more, recur for left 
            return kthSmallest(arr, l, pos-1, k); 
  
        # Else recur for right subarray 
        return kthSmallest(arr, pos+1, r, k-pos+l-1); 
     
  
    # If k is more than number of elements in array 
    return INT_MAX; 
 
  

# It searches for x in arr[l..r], and partitions the array  
# around x. 
def partition(arr, l, r, x):
    for i in range(l,r):
       if (arr[i] == x):
           break
    arr[i], arr[r] = arr[r], arr[i]
    # Standard partition algorithm 
    i = l; 
    for j in range(l,r-1):
        if(arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1
    arr[i], arr[r] = arr[r], arr[i]
    return i; 
 
  
# Driver program to test above methods 

arr = 12, 3, 5, 7, 4, 19, 26;
int n = sizeof(arr)/sizeof(arr[0]), k = 3;
cout << "K'th smallest element is "
     << kthSmallest(arr, 0, n-1, k);

 


























