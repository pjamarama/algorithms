package Fibonacchi;

public class FibonacciRecursion {
    public static void main(String[] args) {
        System.out.println(fibRec(7));
        System.out.println(fibArr(7));
//        range(5);
    }

    public static int fibRec(int n) {
        if (n == 0) {
            return n;
        } else if (n == 1) {
            return n;
        }
        return fibRec(n - 1) + fibRec(n - 2);
    }

    public static int fibArr(int n) {
        int[] fibNumbers = new int[n];
        for (int i = 0; i < n; i++) {

            if (i == 0) {
                fibNumbers[i] = 0;
            } else if (i == 1) {
                fibNumbers[i] = 1;
            } else {
                fibNumbers[i] = fibNumbers[i - 1] + fibNumbers[i - 2];
            }
            System.out.println("i = " + i + "\t" + "fibArr = " + fibNumbers[i]);
        }
        return fibNumbers[n - 1] + fibNumbers[n - 2];
    }

    public static void range(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println(i);
        }
    }
}
