// https://www.codechef.com/COOK109B/problems/COKE

import java.util.*;

class coke{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int n, m, k, l, r, c[], p[], m_price;
       
        while(t-->0)
        {
            n = sc.nextInt();
            m = sc.nextInt();
            k = sc.nextInt();
            l = sc.nextInt();
            r = sc.nextInt();
            c = new int[n];
            p = new int[n];
            m_price = -1;

            for(int i=0; i<n; i++)
            {
                c[i] = sc.nextInt();
                p[i] = sc.nextInt();
            }

            for(int i=0; i<n; i++)
            {
                t = c[i];
                for(int j=0; j<m-1; j++)
                {
                    if(t > k+1)
                    {
                        t--;
                    }
                    else if(t < k-1)
                    {
                        t++;
                    }
                    else
                    {
                        t = k;
                    }
                }

                if(t >= l && t <= r)
                {
                    if(m_price == -1)
                    {
                        m_price = p[i];
                    }
                    else if(p[i] < m_price)
                    {
                        m_price = p[i];
                    }
                }
            }
            System.out.println(m_price);
        }
    }
}
