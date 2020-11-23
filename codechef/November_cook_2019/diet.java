import java.util.*;

class diet{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int a[];
        int total,k;
        while(t-->0)
        {
            n = sc.nextInt();
            k = sc.nextInt();
            a = new int[n];
            total = 0;
            for(int i=0; i<n; i++)
            {
                a[i] = sc.nextInt();
                if (total < 0)
                {
                  continue;
                }
                total += a[i];
                total -= k;
                if (total < 0)
                {
                  System.out.println("NO "+(i+1));
                }
            }
            if(total >= 0)
            {
              System.out.println("YES");
            }
        }
    }
}
