import java.util.*;

class encode{
  public static void main(String args[]) 
  {
    Scanner sc = new Scanner(System.in);
    int t, n, k;
    int e[]; //encoded array
    int o[]; //original array
    int s[]; //sum array
    t = sc.nextInt();
    while(t-->0)
    {
      n = sc.nextInt();
      e = new int[n];
      o = new int[n-1];
      s = new int[n-1];
      for(int i=0; i<n; i++)
      {
        e[i] = sc.nextInt();
      }
      o[0] = e[1];
      s[0] = o[0];

      for(int j=1; j<n-1; j+=1)
      {
        if( j%2 == 0)
        {
          o[j] = e[j+1];
        }
        else
        {
          k = j + 1; 
          k = (int)((Math.log10(k & -k)) / Math.log10(2));
          int index = (j+1) - (int)Math.pow(2, k);
          if(index == 0)
          {
            o[j] = e[j+1] - s[j-1]; 
          }
          else
          {
            o[j] = e[j+1];
            for(int i = index ; i<=j-1 ; i++)
            {
              o[j] -= o[i];                   
            }
          }    
        }
        s[j] = s[j-1] + o[j];
      }
      for(int j=0; j<n-1; j+=1)
      {
        System.out.print(o[j]+" ");
      }
      System.out.println();
    }  
  }
}