// https://www.codechef.com/JUNE20B/problems/XYSTR
import java.util.*;

class xystr{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    String s;
    int sum = 0;

    while(t-->0)
    {
      s = sc.next();
      sum = 0;
    
      char prev = s.charAt(0);
      char curr;
      for(int i=1; i<s.length(); i++)
      {
        curr = s.charAt(i);
        if(Character.compare(prev, curr) != 0)
        {
            sum += 1;
            i++;
        }
        if(i < s.length())
        {
            prev = s.charAt(i);
        }
      }  
      System.out.println(sum);
    }
  }
}

