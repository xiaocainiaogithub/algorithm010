package scr;

class Solution {
    public int climbStairs3(int n) {
    	double sqrt_5=Math.sqrt(5);
    	double fib_n=Math.pow((1+sqrt_5)/2, n+1)-Math.pow((1-sqrt_5)/2, n+1);
    	return (int) (fib_n/sqrt_5);
    }
}
