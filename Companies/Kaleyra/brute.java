import java.util.*;

class brute{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n;
        int prev;
        long total;
        int a[];
        while(t-->0)
        {
            total = 0;
            n = sc.nextInt();
            a = new int[4*n+1];
            for(int i = 4; i <= 4*n; i++)
            {
                prev = 0;
                for(int j = 1; j<=i; j++)
                {   
                    for(int k = 1; k<=i-j; k++)
                    {
                        for(int l = 1; l<=i-j-k; l++)
                        {
                            if(j <= n && k<= n && l<=n)
                            {
                                if(j+k+2*l == i)
                                {
                                    System.out.println(i +" "+ j+" " +" " +k+ " "+l);
                                    prev++;
                                    if(j != k)
                                    {
                                        prev++;
                                    }
                                }
                            }
                             
                        }
                    }
                }
                a[i] = prev; 
                total += prev;
            }
            
            System.out.println(total);
        }
    }
}
