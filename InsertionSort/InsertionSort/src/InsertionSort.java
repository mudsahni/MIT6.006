public class InsertionSort {

    public static int[] insertionSort(int[] A) {
        int n = A.length;
        int temp;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                if (A[j] < A[j - 1]) {
                    temp = A[j - 1];
                    A[j - 1] = A[j];
                    A[j] = temp;
                }
            }
        }
        return A;
    }

    public static void main(String[] args) {
        int[] A = new int[10];
        for (int i = 0; i < 10; i++) {
            A[i] = (int) Math.floor(Math.random() * 30 + 1);
        }
        A = insertionSort(A);
        for (int i = 0; i < A.length; i++) {
            System.out.println(A[i]);
        }
    }

}
