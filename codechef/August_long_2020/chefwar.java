// https://www.codechef.com/AUG20B/problems/CHEFWARS

import java.util.*;

class chefwar{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
		int h, p;
		int winner;

    while(t-->0)
    {
      h = sc.nextInt();
			p = sc.nextInt();
			winner = 1;
			while(h > 0 && p > 0)
			{
				h = h - p;
				p = p/2;
				if(h<=0)
				{
					winner = 1; 
					break;
				}
				else if(p <= 0)
				{
					winner = 0; 
					break;
				}
			}	
	    System.out.println(winner);
    }
  }
}
