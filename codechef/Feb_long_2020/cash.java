// https://www.codechef.com/FEB20B/problems/CASH
import java.util.*;

class cash{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    long n, k, sum;

    while(t-->0)
    {
      n = sc.nextLong();
      k = sc.nextLong();
      sum = 0;
      for(int i =0; i<n; i++)
      {
          sum += sc.nextInt()%k;
      }  
      System.out.println(sum%k);
    }
  }
}
