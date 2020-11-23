https://www.codechef.com/AUG19B/problems/CHEFDIL
import java.util.*;

class chefdil{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        String s;
        int count = 0;
        while(t-->0)
        {
            s = sc.next();
            count = 0;
            for(int i=0; i<s.length(); i++)
            {
                if(s.charAt(i) == '1')
                {
                    count++;
                }
            }
            if(count % 2 == 0)
            {
                System.out.println("LOSE");
            }
            else
            {
                System.out.println("WIN");
            }
        }
    }
}
