import java.util.*;

class lunch_june_2019{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int a[];
        while(t-->0)
        {
            n = sc.nextInt();
            a = new int[n];
            for(int i=0; i<n; i++)
            {
                a[i] = sc.nextInt();
            }

            Arrays.sort(a);
            System.out.println("Arrays is "+Arrays.toString(a));
            for(int i=0; i<n; i++)
            {
                System.out.println(a[i]);
            }
        }
    }
}
