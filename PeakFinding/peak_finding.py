import random
import time

# linear search
def find_peak_linear(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    
    peak = array[0]
    for i in range(2, len(array)):
        if array[i] > array[i - 1]:
            temp = array[i]
        else:
            temp = array[i - 1]
        
        if temp > peak:
            peak = temp
    return peak


def find_peak_recursive(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            return array[1]

    n = len(array)
    if array[n // 2 - 1] > array[n // 2 + 1]:
        if array[n // 2] > array[n // 2 - 1]:
            return array[n//2]
        else:
            return find_peak_recursive(array[: n // 2])
    else:
        if array[n // 2] > array[n // 2 + 1]:
            return array[n // 2]
        else:
            return find_peak_recursive(array[n // 2 :])


# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# print(find_peak_linear(array))
# print(find_peak_recursive(array))

def check_peak(array, prediction):
    if type(array) != list or len(array) == 0:
        return True
    return max(array) == prediction

def test(n):
    for i in range(0, n, 10):
        print("=" * 10)
        print(f"finding peak for range {i}")
        for j in range(0, 1000, 10):
            print("*"*10)
            print(f"array length: {j}")
            array = [random.randint(0, i) for i in range(j)]
            t1l = time.time()
            peak1 = find_peak_linear(array)
            t2l = time.time()
            t1r = time.time()
            peak2 = find_peak_recursive(array)
            t2r = time.time()
            print(f"Predicted linear peak: {peak1}")
            print(f"Predicted recursive peak: {peak2}")
            print(f"Time taken linear: {t2l - t1l}")
            print(f"Time taken recursive: {t2r - t1r}")
            is_correct1 = check_peak(array, peak1)
            is_correct2 = check_peak(array, peak2)
            print(f"peak difference: {peak1 - peak2}")
            print(f"is correct linear? {is_correct1}")
            print(f"is correct recursive? {is_correct2}")
            print("*" * 10)
        print("=*10")


print(find_peak_recursive([1,3,20,4,1,0]))