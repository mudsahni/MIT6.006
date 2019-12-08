const binarySearch = (A, x) => {
    const n = A.length
    if (n == 1) {
        return A[0] == x
    }

    let mid = Math.floor(n / 2)
    if (A[mid] > x) {
        return binarySearch(A.slice(0,mid), x)
    } else if (A[mid] < x) {
        return binarySearch(A.slice(mid+1, n), x)
    } else {
        return A[mid] == x
    }
}

const A = [9, 10, 13, 15, 19, 21, 33, 41]
console.log(binarySearch(A, 33))