// https://www.codechef.com/OCT20B/problems/CVDRUN
import java.util.*;

class covid_run{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int n, x, y, k, total = 0;
		boolean flag = false;

    while(t-->0)
    {
			n = sc.nextInt();
			k = sc.nextInt();
			x = sc.nextInt();
			y = sc.nextInt();
			flag = false;
			if(n%2 != 0 || x == y)
			{
				 flag = true; 
			}
			else
			{
				k = k%n;
				for(int i=0; x != total; i++)
				{
					if(i == 0)
					{
						total = x; 
					}
					total = (total + k)%n; 		
					if(total == y)
					{
						flag = true;
					}
				}
			}
			if(flag == true)
			{
				System.out.println("YES");
			}
			else 
			{
				System.out.println("NO");
			}
    }
  }
}
