
def binary_search(A, x):
    n = len(A)
    if len(A) == 1:
        return A[0] == x
    
    mid = n//2
    if x > A[mid]:
        return binary_search(A[mid+1:], x)
    elif x < A[mid]:
        return binary_search(A[:mid], x)
    else:
        return A[mid] == x

    
A = [9,10,13,15,19,21,33,41]
print(binary_search(A, 55))