import java.util.Arrays;

public class BinarySearch {

    public static boolean binarySearch(int[] A, int x) {
        int n = A.length;
        if (n == 1) {
            return A[0] == x;
        }

        int mid = n / 2;
        if (A[mid] > x) {
            return binarySearch(Arrays.copyOfRange(A, 0, mid), x);
        } else if (A[mid] < x) {
            return binarySearch(Arrays.copyOfRange(A, mid + 1, n), x);
        } else {
            return A[mid] == x;
        }

    }

    public static void main(String[] args) {
        int[] A = {9, 10, 13, 15, 19, 21, 33, 41};
        System.out.println(binarySearch(A, 33));
    }
}
