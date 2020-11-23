// https://www.codechef.com/LTIME78B/problems/DEADEND
import java.util.*;

class plant_trees{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n, total;
        int a[];
        boolean flag;
        // int total,k;
        while(t-->0)
        {
            n = sc.nextInt();
            a = new int[n];
            total = 0;
            for(int i=0; i<n; i++)
            {
                a[i] = sc.nextInt();
            }

            Arrays.sort(a);
            // System.out.println("Arrays is "+Arrays.toString(a));
            for(int i=0; i<n-1; i++)
            {
              if(a[i+1] - a[i] >= 2)
              {
                // i++;
                total++;
              }
            //   else if(a[i+1]-a[i] >= 2)
            //   {
            //     total++;
            //   }
            }
            if(n>=2 && a[n-1] - a[n-2] > 2)
            {
              total += 1;

            //   if(n == 2)
            //   {
            //     total++;
            //   }
            }
            // if(n>=3 && a[n-2] - a[n-3] >= 2)
            // {
            //   total++;
            // }
            System.out.println(total);
        }
    }
}
