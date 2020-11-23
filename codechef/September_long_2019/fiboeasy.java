import java.util.*;

class fiboeasy{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        long p, f, s, ans;
        long n;
        while(t-->0)
        {
            f = 0; s = 1;
            ans = 0;
            n = sc.nextLong();
            // p = (long)(Math.log(n) /  Math.log(2)); 
            // p = (long)Math.pow(2, p);
            while(true)
            {

            }
            p = p % 60;
            // System.out.println("p is " + p);
            for(long i=0; i<p-2; i++)
            {
                ans = f + s;
                f = s;
                s = ans;
            }
            // System.out.println("ans : "+ans);
            System.out.println(ans%10);
        }
    }
}
