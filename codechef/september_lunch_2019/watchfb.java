// https://www.codechef.com/LTIME76B/problems/WATCHFB
import java.util.*;

class watchfb
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t, n, score;
        long team, a, b;
        int fteam, oteam;
        t = sc.nextInt();
        while(t-->0)
        {
            n = sc.nextInt();
            fteam = 0;
            oteam = 0;
            for(int i=0; i<n; i++)
            {
                team = sc.nextLong();
                a = sc.nextLong();
                b = sc.nextLong();
                if(team == 1 || (a == b))
                {
                    System.out.println("YES");
                    fteam = a;
                    oteam = b;
                    
                }
                else if(i == 0)
                {
                    System.out.println("NO");
                    fteam = 0
                    oteam = 0
                    
                }
                // compare scores with fteam 
                else if(fteam < a && fteam >= b)
                {
                    fteam = b;
                    oteam = a;
                    System.out.println("YES");
                    
                }
                else if(fteam < b && fteam >= a)
                {
                    fteam = a;
                    oteam = b;
                    System.out.println("YES");
                    
                }
                // compare scores with oteam
                else if(oteam < a && oteam >= b)
                {
                    fteam = a;
                    oteam = b;
                    System.out.println("YES");
                    
                }
                else if(oteam < b && oteam >= a)
                {
                    fteam = b;
                    oteam = a;
                    System.out.println("YES");
                    
                }
                else
                {
                    System.out.println("NO");
                    fteam = 0;
                    oteam = 0;
                }
                
            }    
        }
    }
}
