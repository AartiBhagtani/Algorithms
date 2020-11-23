// https://www.codechef.com/AUG20B/problems/CRDGAME3
import java.util.*;

class pattern{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int pc, c, pr, r;
    
    while(t-->0)
    {
      pc = sc.nextInt();
			pr = sc.nextInt();
			c = pc/9;
			r = pr/9;
			if(pc % 9 != 0)
			{
				c++;
			}
			if(pr % 9 != 0)
			{
				r++;
			}
			if(r <= c)
			{
				System.out.println("1 "+r);
			}
			else
			{
				System.out.println("0 "+c);
			}
		}
  }
}
