// https://www.codechef.com/AUG20B/problems/CHEFWED
import java.util.*;

class chefwed{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int n, k, fights, tables, tables_2;
		int arr[];
		int freq_arr[];
		HashSet<Integer> hset;

    while(t-->0)
    {
      n = sc.nextInt();
			k = sc.nextInt();
			fights = 0;
			tables = 1; 
			tables_2 = 1; 
			hset = new HashSet<Integer>(); 
			arr = new int[n];
		  freq_arr = new int[101];
			for(int i=0; i<n; i++)
			{
				arr[i] = sc.nextInt();
				freq_arr[arr[i]]++;
			}

			for(int i=1; i<=100; i++)
			{
				if(freq_arr[i] > 1)
				{
					fights += freq_arr[i];
				}
			}

			hset.add(arr[0]);
			for(int i=1; i<n; i++)
			{
				if(hset.contains(arr[i]) == true)
				{
					hset.clear();
					tables++;
				}
				hset.add(arr[i]);
			}
			hset.clear();
			hset.add(arr[n-1]);
			for(int i=n-2; i>0; i--)
			{
				if(hset.contains(arr[i]) == true)
				{
					hset.clear();
					tables_2++;
				}
				hset.add(arr[i]);
			}
			int minm = k + fights;
			if(minm > (k * tables))
			{
				minm = k * tables;
			}
			if(minm > (k * tables_2))
			{
				minm = k * tables_2;
			}			
	    System.out.println(minm);
    }
  }
}

