import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int[] A=new int[N];
		for(int i=0;i<N;i++){
			A[i]=sc.nextInt();
		}
		// Arrays.sort(A);
		int i,j,k,count=0;
		for(i=0;i<N;i++){
			for(j=i+1;j<N;j++){
				for(k=j+1;k<N;k++){
                    System.out.println(A[i]);
				    System.out.println(A[j]);
				    System.out.println(A[k]);
				    System.out.println();
					if(getIfGood(A[i],A[j],A[k])) count+=6;
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
