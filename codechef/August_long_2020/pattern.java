// https://www.codechef.com/AUG20B/problems/SKMP
import java.util.*;

class pattern{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    String s, p, final_string;
    int arr[];
    boolean max,set;

    while(t-->0)
    {
      s = sc.next();
      p = sc.next();
			arr = new int[26];
      final_string = "";
      max = false;
      set = false;

      for(int i=0; i<s.length(); i++)
      {
        int index = (int)s.charAt(i);
				arr[index-97]++;
      }

      int prev = (int)p.charAt(0);
      arr[prev-97]--;
      
      for(int i=1; i<p.length(); i++)
      {
        int index = (int)p.charAt(i);
        arr[index-97]--;
        if(set == false && index != prev)
        {
          set = true;
          if(index < prev)
          {
            max = true;
          }
        }
      }
      
			int value = (int)p.charAt(0) - 97;
			for(int i=0; i<arr.length; i++)
      {
        if(value == i && max == true)
				{
					final_string += p;
				}
				char[] repeat = new char[arr[i]];
				Arrays.fill(repeat, (char)(i+97));
				final_string += new String(repeat);
				if(value == i && max == false)
				{
					final_string += p;
				}
			}
			System.out.println(final_string);
    }
  }
}
