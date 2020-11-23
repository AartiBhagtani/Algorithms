// https://www.codechef.com/JUNE20B/problems/EOEO
import java.util.*;

class eoeo{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    long ts;
    long ans;

    while(t-->0)
    {
      ans = 0; 
      ts = sc.nextLong();
      if(ts%2 != 0)
      {
          ans = ts/2; 
      }
      else
      {
          while(true)
          {
              ts = ts/2;
              if(ts%2 != 0 || ts == 0) 
              {
                  break;
              }
          }
          ans = ts/2;
      }
      System.out.println(ans);
    }
  }
}
