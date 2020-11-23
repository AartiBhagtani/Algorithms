import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.StringTokenizer; 

class max_sum{
  public static void main(String args[])throws IOException 
  {
    BufferedReader br = new BufferedReader( 
      new InputStreamReader(System.in)); 
    StringTokenizer st = new StringTokenizer(br.readLine()); 

    int t = Integer.parseInt(st.nextToken()); 
    int n, k, count, length;
    boolean flag, contains;
    int a[];
    
    while(t-->0)
    {
      n = Integer.parseInt(br.readLine()); 
      k = Integer.parseInt(br.readLine()); 
      a = new int[n];
      // System.out.println(n);

      count = 0; flag = false; contains = false; length= 0;
      for(int i = 0; i<n; i++)
      {
        // System.out.println(a[i]);
        a[i] = Integer.parseInt(st.nextToken()); 
          // System.out.println(a[i]);
        // a[i] = sc.nextInt();
        if(a[i] <= k)
        {
          length ++;
          if(flag == false)
          {
            flag = true;
            
          }
          if(k == a[i]) 
          {
            // System.out.println("in contains"+a[i]);
            contains = true;
          }
        }
        else
        { 
          if(flag == true)
          {
            if(contains == true)
            {
              count += length;
              contains = false;
            }
            flag = false;
            length = 0;
          }
        }
      }

      if(a[n-1] <= k)
      {
        if(contains == true || a[n-1] == k)
        {
          count += length;
        }
      }
      System.out.println(count);
    }
  }
}
