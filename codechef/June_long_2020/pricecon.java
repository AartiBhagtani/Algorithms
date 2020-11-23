// https://www.codechef.com/JUNE20B/problems/PRICECON
import java.util.*;

class pricecon{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n,k;
    int a[];
    int sum = 0; 
    while(t-->0)
    {
      n = sc.nextInt();
      k = sc.nextInt();
      a = new int[n];
      sum = 0;
      for(int i =0; i<n; i++)
      {
          a[i] = sc.nextInt();
          if(a[i] > k)
          {
              sum += a[i] - k;
          }
      }  
      System.out.println(sum);
    }
  }
}
