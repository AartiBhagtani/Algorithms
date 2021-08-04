// https://www.codechef.com/COOK109B/problems/COKE

import java.util.*;
import java.lang.Math;

class prob4{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    
    while(t-->0)
    {
      int a = sc.nextInt();
      int b = sc.nextInt();
       
      int x = b - a;
      if(a > b)
        x = a;
      int ans1 = (int)Math.ceil((b-x)/2.0);
      int ans2 = (int)Math.ceil((x-a)/2.0);
      
      System.out.println(ans1 + ans2);
    }
  }
}
