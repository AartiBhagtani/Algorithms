// https://www.codechef.com/JUNE20B/problems/EVENM
// https://www.codechef.com/JUNE20B/problems/PRICECON
import java.util.*;

class evenm{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n, count, tmp;

    // n = 1 handle

    while(t-->0)
    {
      n = sc.nextInt();
      count = 1; 

      if(n%2 == 0)
      {
        for(int i=1; i<=n; i++)
        {
          tmp = count;  
          if(i%2 == 0)
            tmp += n-1;  
          for(int j=1; j<=n; j++)
          {
            if(i%2 == 0)
            {   
                System.out.print(tmp+" ");          
                tmp--;
            }
            else
            {
                System.out.print(count+" ");       
            }
            count++;
          }
          System.out.println();
        }
      }
      else
      {
        for(int i=1; i<=n; i++)
        {
          for(int j=1; j<=n; j++)
          {
                System.out.print(count+" ");    
                count++;
          }
          System.out.println();
        } 
      }
    }
  }
}
