// https://www.codechef.com/AUG20B/problems/LINCHESS

import java.util.*;

class linearchess{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int n, k;
		int arr[];
		int total_moves;
		int moves, win_pawn;

    while(t-->0)
    {
      n = sc.nextInt();
			k = sc.nextInt();
			arr = new int[n];
			total_moves = Integer.MAX_VALUE;
			moves = 0;
			win_pawn = -1; 
			for(int i=0; i<n; i++)
			{
				arr[i] = sc.nextInt();
			}
			for(int i=0; i<n; i++)
			{
				if(arr[i] < k)
				{
					int pawn = arr[i];
					moves = 0;
					while(pawn <= k)
					{
						pawn += arr[i];
						moves++;
						if(pawn == k && moves < total_moves) 
						{
							total_moves = moves;
							win_pawn = arr[i];
						}
					}
				}
			}
	    System.out.println(win_pawn);
    }
  }
}
