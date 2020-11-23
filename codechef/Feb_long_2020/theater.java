// https://www.codechef.com/FEB20B/problems/THEATRE
import java.util.*;

class theater{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n, a[][];
    int sum1, sum2, sum;
    int total_sum = 0;
    int i = 0, j = 0; 
    int max_time = 0; 

    while(t-->0)
    {
      n = sc.nextInt();  
      a = new int[5][5];
      sum = 0;

      
      for(i =0; i<n; i++)
      { 
          int movie = sc.next().charAt(0) - 64;
          int time = sc.nextInt();
          HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>(){{
            put(12, 1);
            put(3, 2);
            put(6, 3);
            put(9, 4);
          }};
          a[movie][hm.get(time)] += 1;
      }  
      boolean check_time[] = new boolean[5];
      int ab[] = new int[5];
    
      //   i movie
      //   i time
      max_time = 0;
      for(i=1; i<5; i++)
      {  
        int prev = 0;
        for(j=1; j<5; j++)
        {
            if(a[j][i] > prev && !check_time[j])
            {
                prev = a[j][i]; 
                max_time = j;
            }
        }                 
        check_time[max_time] = true;
        ab[i] = prev;
      }  
     
      Arrays.sort(ab); 
      sum1= ab[4]*100 + ab[3]*75 + ab[2]*50 + ab[1]*25;
      for(i=1; i<5; i++)
      {
          if(ab[i] == 0)
          {
              sum1 -= 100;
          }
      }
      //2nd approach
      for(i=1; i<5; i++)
      {
        check_time[i] = false;
      }

      for(i=1; i<5; i++)
      {  
        int prev = 0;
        for(j=1; j<5; j++)
        {
            if(a[i][j] > prev && !check_time[i])
            {
                prev = a[i][j]; 
                max_time = i;
            }
        }                 
        check_time[max_time] = true;
        ab[i] = prev;
      }  
     
      Arrays.sort(ab); 
      sum2 = ab[4]*100 + ab[3]*75 + ab[2]*50 + ab[1]*25;
      for(i=1; i<5; i++)
      {
          if(ab[i] == 0)
          {
              sum2 -= 100;
          }
      }

      sum = sum1>=sum2 ? sum1 : sum2;
      
      System.out.println(sum);
      total_sum += sum;
    }
    System.out.println(total_sum);
  }
}