
import time

def find_1d_peak(array, low, high, n):
    #n = len(array)
    # base case
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return max(array)

    mid = (low + (high - low))//2
    if array[mid] >= array[mid - 1] and array[mid] >= array[mid + 1]:
        return array[mid]
    else:
        if array[mid - 1] > array[mid + 1]:
            return find_1d_peak(array, low, mid-1, n)
        else:
            return find_1d_peak(array, mid+1, high, n)
    

def findPeakUtil(arr, low, high, n):

    # Find index of middle element
    # (low + high)/2
    mid = low + (high - low)/2
    mid = int(mid)

    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
        (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return mid 


    # If middle element is not peak and  
    # its left neighbour is greater  
    # than it, then left half must  
    # have a peak element 
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return findPeakUtil(arr, low, (mid - 1), n) 

    # If middle element is not peak and 
    # its right neighbour is greater 
    # than it, then right half must  
    # have a peak element 
    else: 
        return findPeakUtil(arr, (mid + 1), high, n) 
  

def findPeak(arr, n):

    return findPeakUtil(arr, 0, n - 1, n)

import random
a = [random.randint(0, 10000) for i in range(1000000)]
n = len(a)
t1a = time.time()
print(find_1d_peak(a, 0, n-1, n))
t1b = time.time()
print(f"Time taken 1: {t1b - t1a}")
t2a = time.time()
print(a[findPeak(a, n)])
t2b = time.time()
print(f"Time taken 2: {t2b - t2a}")
print(f"Faster? t1 > t2: {(t2b-t2a) > (t1b-t1a)}")