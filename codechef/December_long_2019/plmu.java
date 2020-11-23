import java.util.*;

class plmu{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int a[];
        int total;
        while(t-->0)
        {
            n = sc.nextInt();
            a = new int[n];
            total = 0;
            for(int i=0; i<n; i++)
            {
                a[i] = sc.nextInt();
            }
            for(int i=0; i<n; i++)
            {
                for(int j=i+1; j<n; j++)
                {
                    if(a[i]*a[j] == a[i]+a[j])
                    {
                        total++;
                    }
                }
            }
            System.out.println(total);
        }
    }
}
