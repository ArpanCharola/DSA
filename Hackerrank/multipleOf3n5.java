import java.util.Scanner;

public class multipleOf3n5 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int a0 = 0; a0 < t; a0++) {
            long n = in.nextLong();
            // We need the sum below n, so use n-1
            long target = n - 1;
            
            long sum3 = sumMultiples(target, 3);
            long sum5 = sumMultiples(target, 5);
            long sum15 = sumMultiples(target, 15);
            
            System.out.println(sum3 + sum5 - sum15);
        }
    }

    private static long sumMultiples(long n, long k) {
        long m = n / k;
        return k * (m * (m + 1) / 2);
    }
}