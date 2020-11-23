// https://www.codechef.com/JUNE20B/problems/COVDSMPL
import java.util.*;

class covid_sample{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n, p, i, j, x, sum;
    int arr[][];
    boolean flag;

    while(t-->0)
    {
      n = sc.nextInt();
      p = sc.nextInt();
      arr = new int[n][n];
      sum = 0;  
      flag = false; 

      p = n * n * p / 100; 
        
      for(i=1; i<n; i+=2)
      {
        for(j=1; j<n; j+=2)
        {
            System.out.println("1 "+i+" "+j+" "+(i+1)+" "+(j+1));
            x = sc.nextInt();
            if(x < 4)
            {
							
            }
            else if(x == 4)
            {
                arr[i][j] = 1;
                arr[i][j+1] = 1;
                arr[i+1][j] = 1;
                arr[i+1][j+1] = 1;
            }
            if(x != -1)
            {
                sum += x;
                if(sum == p)
                {
                    // flag = true; 
                    break;
                }
            }
        }
			} 
			if(sum == p)
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
					System.exit(0);
				}
			} 
    }
  }
}
