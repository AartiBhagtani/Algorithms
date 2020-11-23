// https://www.codechef.com/AUG20B/problems/CHEFWED
import java.util.*;

class chefwed_1{

	static int fights(int arr[], int a, int b)
	{
		int fights = 0; 
    HashMap<Integer, Integer> hmap =  new HashMap<>();
		for(int i=a; i<=b; i++)
		{
			if(hmap.containsKey(i))  
			{
				hmap.put(i, hmap.get(i)+1);
			}
			else
			{
				hmap.put(a,1);
			}
		}
		for (Integer nfights : hmap.values())  
		{
			if(nfights > 1)
			{
				fights += nfights;
			}
		}       
    return fights;
	}
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int n, k;
		int arr[], dp[];

    while(t-->0)
    {
      n = sc.nextInt();
      k = sc.nextInt();
			arr = new int[n]; 
			dp = new int[n+1]; 
			for(int i=0; i<n; i++)
			{
				arr[i] = sc.nextInt();
			}
			dp[1] = k; 
			for(int i=2; i<=n; i++)
			{
				dp[i] = dp[i-1] + k;
				for(int j=i-1; j>=1; j--)
				{
					System.out.println(fights(arr, j, i));
					dp[i] = Math.min(dp[i], dp[j-1] + k + fights(arr, j, i) );
				}
			}
			System.out.println(dp[n]);
    }
  }
}
