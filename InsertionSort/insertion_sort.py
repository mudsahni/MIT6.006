import numpy as np 

A = list(np.random.randint(0, 30, (1, 10)).reshape(-1))
print(A)

def insertion_sort(A):
    n = len(A)
    for i in range(n):
        for val in range(1,n):
            if A[val] < A[val-1]:
                A[val-1], A[val] = A[val], A[val-1]

    return A

print(insertion_sort(A))