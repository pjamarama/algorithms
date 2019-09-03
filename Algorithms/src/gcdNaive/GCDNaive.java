package gcdNaive;

public class GCDNaive {
    public static void main(String[] args) {
        int a = 2359933*123;
        int b = 1323943*123;
        System.out.println("GCD: " + findGCD(a, b));
    }

    public static int findGCD(int a, int b){
        int gcd = 0;
        for (int i = 1; i <= Math.min(a, b); i++){
            if (Math.max(a, b) % i == 0 && Math.min(a, b) % i ==0){
                gcd = i;
//                System.out.println(gcd);
            }
        }
        return gcd;
    }
}
