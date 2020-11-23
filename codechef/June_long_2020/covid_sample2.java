// https://www.codechef.com/JUNE20B/problems/COVDSMPL
import java.util.*;

class covid_sample2{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n, p, i, j, x, sum, total;
    int arr[][];

    while(t-->0)
    {
      n = sc.nextInt();
      p = sc.nextInt();
      arr = new int[n+1][n+1];
      sum = 0;  

      System.out.println("1 "+"1 "+"1 "+n+" "+n);
      total = sc.nextInt();

      outerloop:
      {  
        for(i=1; i<=n; i++)
        {
          for(j=1; j<=n; j++)
          {
            System.out.println("1 "+i+" "+j+" "+(i)+" "+(j));
            x = sc.nextInt();
            if(x == 1)
            {
                arr[i][j] = 1;
                sum += x;
            }
            if(x != -1)
            {
              if(sum == total)
              {
                  break outerloop;
              }
              
            }   
          }
        } 
      }  
			if(sum == total)
			{
				System.out.println("2");
				for(i=1; i<=n; i++)
      	{
        	for(j=1; j<=n; j++)
        	{
						System.out.print(arr[i][j]+" ");
					}
					System.out.println();
				}
				x = sc.nextInt();
				if(x == -1)
				{
					break;
				}
			} 
    }
  }
}
