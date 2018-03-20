/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

public class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int i;
		int t = sc.nextInt();
		while(t!=0)
		{
		    //System.out.println(t);
		    int n = sc.nextInt();
		    int a[] = new int[n];
		    int b[] = new int[n];
		    for(i=0;i<n;i++)
		    {
		        a[i] = sc.nextInt();
		    }
		    for(i=0;i<n;i++)
		    {
		        b[i] = sc.nextInt();
		    }
		    int maxa = getMax(a);
		    int maxb = getMax(b);
		    a[maxa] = 0;
		    b[maxb] = 0;
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
		}
	}

    public static int getMax(int[] inputArray){
        int maxValue = inputArray[0];
        int maxindex = 0;
        for(int i=1;i < inputArray.length;i++){
          if(inputArray[i] > maxValue){
             maxValue = inputArray[i];
             maxindex = i;
          }
        }
        return maxindex;
      }
}
