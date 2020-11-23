// https://www.codechef.com/JUNE20B/problems/CHFICRM
import java.util.*;

import javax.lang.model.util.ElementScanner6;

class chficrm{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n;
    ArrayList<Integer> data;
    int ele;
    boolean flag;

    while(t-->0)
    {
      n = sc.nextInt();
      data = new ArrayList<>();
      flag = false;  
      for(int i=0; i<n; i++)
      {
        ele = sc.nextInt();
        if(ele == 5)
        {
            data.add(ele);
        }
        else if(ele == 10)
        {
            if(data.contains(5))
            {
                data.remove(new Integer(5));
                data.add(new Integer(10));
            }
            else
            {
                flag = true;
            }
        }
        else
        {
            if(data.contains(10))
            {
                data.remove(new Integer(10));
                data.add(new Integer(15));
            }
            else if(data.contains(5))
            {
                data.remove(new Integer(5));
                if(data.contains(5))
                {
                    data.remove(new Integer(5));
                    data.add(new Integer(15));     
                }
                else
                {
                    data.add(new Integer(5));
                    flag = true;
                }
            }
            else 
            {
                flag = true;
            }
        }
      }
      data.clear();
      if(flag == false)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }

    }
  }
}

