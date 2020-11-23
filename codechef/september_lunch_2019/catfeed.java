// https://www.codechef.com/LTIME76B/problems/CATFEED
import java.util.*;

class catfeed
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t, n, m, count, an[], am[];
        boolean flag;
        t = sc.nextInt();
        while(t-->0)
        {
            flag = true;
            count = 0;
            n = sc.nextInt();
            m = sc.nextInt();
            an = new int[n+1];
            am = new int[m+1];
            for(int i=1; i<=m; i++)
            {
                am[i] = sc.nextInt();
            }
            for(int i=1; i<=m; i++)
            {
                if((i-1)%n == 0)
                {
                    count++;
                }
                an[am[i]] += 1;
                // System.out.println("count = "+count+" am[i] + "+am[i]+" an[am[i]] = "+an[am[i]]);
                if(an[am[i]] > count)
                {
                    flag = false;
                    break;
                }
            }
            if(flag)
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
