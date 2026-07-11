import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        
        for (int a0 = 0; a0 < t; a0++) {
            long n = in.nextLong();
            
            // Starting even Fibonacci numbers
            long a = 2; // E1
            long b = 8; // E2
            long sum = a;
            
            // Check if second term is within limit before starting loop
            if (n >= 8) {
                sum += b;
            }
            
            while (true) {
                long next = 4 * b + a;
                if (next > n) break;
                
                sum += next;
                a = b;
                b = next;
            }
            
            System.out.println(sum);
        }
    }
    public static long sumEvenFibonacci(long n) {
        long a = 2; // E1
        long b = 8; // E2
        long sum = a;
        
        if (n >= 8) {
            sum += b;
        }
        
        while (true) {
            long next = 4 * b + a;
            if (next > n) break;
            
            sum += next;
            a = b;
            b = next;
        }
        
        return sum;
    }
}