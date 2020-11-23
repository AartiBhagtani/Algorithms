// https://www.codechef.com/JUNE20B/problems/EVENM
// https://www.codechef.com/JUNE20B/problems/PRICECON
import java.util.*;

class evenm{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int n, l, r, prev;
		boolean result; 

    // n = 1 handle

    while(t-->0)
    {
			l = sc.nextInt();
			r = sc.nextInt();
			n = r;
			prev = n % l; 
			result = false; 
			for(int i=l+1; i<=r; i++)
			{	
				if(n % i > prev)
				{
					prev = n % i; 
				}
				else
				{	
					result = true; 
					break;
				}
			}
			if (result)
    }
  }
}
