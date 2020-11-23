// https://www.codechef.com/AUG19B/problems/DSTAPLS
import java.util.*;

class distributeApples{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    long n, k;

    while(t-->0)
    {
      // n = apples
      // k = boxes
      n = sc.nextLong();
      k = sc.nextLong();
                  
      if(n/k % k == 0)
      {
          System.out.println("NO");
      }
      else
      {
          System.out.println("YES");
      } 
    }
  }
}
