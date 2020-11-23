// hackerearth good triples

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger; 


/* Name of the class has to be "Main" only if the class is public. */
class triples
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int[] A=new int[101];
		for(int i=1;i<=N;i++){
			A[sc.nextInt()] += 1;
        }
        BigInteger flagi, flagj, flagk;
        int i,j,k;
        BigInteger count = new BigInteger("0");
		for(i=1;i<=100;i++){
		    if(A[i] == 0) continue;
			for(j=1;j<=100;j++){
			    if(A[j] == 0) continue;
			    if(j == i && A[j] <=1) continue;
				for(k=1;k<=100;k++){
                    if(A[k] == 0) continue;
                    if(i == j && j == k) continue;
                    if((k == j || k == i) && (A[k] <= 1)) continue; 
				    
                    if(getIfGood(i,j,k))
                    {
                        String a = String.valueOf(A[i]);
                        String b = String.valueOf(A[j]);
                        String c = String.valueOf(A[k]);
                        flagi = new BigInteger(a);
                        flagj = new BigInteger(b);
                        flagk = new BigInteger(c);
                        BigInteger one = new BigInteger("1");

                        if(i == j)
                        {
                            flagj = flagj.subtract(one); 
                        }
                        else if(j == k)
                        {
                            flagk = flagk.subtract(one); 
                        }
                        else if(k == i)
                        {
                            flagk = flagk.subtract(one);   
                        }
                        flagi = flagi.multiply(flagj);
                        flagj = flagi.multiply(flagk);
                        count = count.add(flagj);
                    }
				}
			}
		}
		System.out.println(count);
	}
	
	static boolean getIfGood(int a, int b, int c){
		int count=0,sum=a+b+c;
		if(sum%a==0) count++;
		if(sum%b==0) count++;
		if(sum%c==0) count++;
		if(count==1) return true;
		return false;
	}
}
