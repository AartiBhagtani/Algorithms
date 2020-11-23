// https://www.codechef.com/AUG19B/problems/MSNSADM1
import java.util.*;

class football{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int max, a[], b[];
        while(t-->0)
        {
            n = sc.nextInt();
            a = new int[n];
            b = new int[n];

            for(int i=0; i<n; i++)
            {
                a[i] = sc.nextInt() * 2;
            }

            max = 0;

            for(int i=0; i<n; i++)
            {
                b[i] = a[i] - sc.nextInt();
                if(b[i] > max)
                {
                    max = b[i];
                }
            }
            System.out.println(max*10);
        }
    }
}
