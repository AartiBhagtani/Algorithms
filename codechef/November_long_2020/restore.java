// https://www.codechef.com/NOV20B/problems/RESTORE
import java.util.*;

class restore{

  static int find_prime(int n)
  {
    boolean flag;
    while(true)
    {
      flag = false;
      for(int i=2; i <= n/2; i++)
      {
        if(n % i == 0)
        {
          flag = true;
          break;
        }
      }
      if(flag == false)
      {
        return n;
      }
      n++;
    }
  }
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n, a[], b[], last_prime, large;
    while(t-->0)
    {
      n = sc.nextInt();
      a = new int[n+1];
      b = new int[n+1];
      large = 4000000;  
      last_prime = 1; 

      for(int i=1; i<=n; i++)
      {
        b[i] = sc.nextInt(); 
      }

      for(int i=1; i<=n; i++)
      {
        if(a[i] != 0) 
        {
          continue;
        }
        if(i == b[i])
        {
          a[i] = large;
          large--;
        }
        else
        {
          if(a[b[i]] == 0)
          {
            a[b[i]] = find_prime(last_prime + 1);
            last_prime = a[b[i]];
          }
          a[i] = a[b[i]];  
        }
      }

      for(int i=1; i<=n; i++)
      {
        System.out.print(a[i] + " "); 
      }
    }
    System.out.println();  
  }
}
