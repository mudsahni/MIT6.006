
const insertionSort = (A) => {
    const n = A.length;
    let temp;
    for (let i = 0; i < n; i++) {
        for (let j = 1; j < n; j++) {
            if (A[j] < A[j - 1]) {
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
            }
        }
    }
    return A;
}

A = []
for (let i = 0; i < 10; i++) {
    A.push(Math.floor(Math.random() * 30) + 1)
}
console.log(A)
console.log(insertionSort(A))