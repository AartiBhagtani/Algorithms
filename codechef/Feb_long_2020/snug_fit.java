// https://www.codechef.com/FEB20B/problems/SNUG_FIT
import java.util.*;

import javax.lang.model.util.ElementScanner6;

class snug_fit{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    long n, a[], b[];
    long sum;

    while(t-->0)
    {
      n = sc.nextInt();  
      a = new int[n];
      b = new int[n];
      sum = 0;
      for(int i =0; i<n; i++)
      {
          a[i] = sc.nextLong();
      }  

      for(int i=0; i<n; i++)
      {
          b[i] = sc.nextLong();
      }  
     
      Arrays.sort(a); 
      Arrays.sort(b); 

      for(int i=0; i<n; i++)
      {
          if(a[i] <= b[i])
          {
            sum += a[i];
          }
          else 
          {
            sum += b[i];
          }
      }

      System.out.println(sum);
    }
  }
}
