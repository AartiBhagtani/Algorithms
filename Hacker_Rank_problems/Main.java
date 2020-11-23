/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class GFG {
	System.out.print();ublic static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int i;
		int t = sc.nextInt();
		while(t!=0)
		{

		    //System.out.println(t);
		    int n = sc.nextInt();
		    int a[] = new int[n];
		    int b[] = new int[n];
		    int maxai = 0;
		    int maxbi = 0;
		    int maxa = 0;
		    int maxb = 0;

		    for(i=0;i<n;i++)
		    {
		        a[i] = sc.nextInt();
		        if(a[i]>maxa)
		        {
		            maxa = a[i];
		            maxai = i;
		        }
		    }
		    for(i=0;i<n;i++)
		    {
		        b[i] = sc.nextInt();
		        if(b[i]>maxb)
		        {
		            maxb = b[i];
		            maxbi = i;
		        }
		    }

		    a[maxai] = 0;
		    b[maxbi] = 0;
		    int suma = 0;
		    int sumb = 0;
		    for(i=0;i<n;i++)
		    {
		        suma = suma + a[i];
		        sumb = sumb + b[i];
		    }
		    //System.out.println(suma+" "+sumb);
		    if(suma<sumb)
		    {
		        System.out.println("Alice");
		    }
		    else if(suma>sumb)
		    {
		        System.out.println("Bob");
		    }
		    else
		    {
		        System.out.println("Draw");
		    }
		    t--;
    }
	}
}
