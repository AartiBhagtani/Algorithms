import java.util.*;

class post_integer{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    while(t-->0)
    {
      int n = sc.nextInt();
      int k = sc.nextInt();
      for(int i=1; i<=k; i++)
      {
        System.out.print(i+" ");
      }
      for(int i=k+1; i<=n; i++)
      {
        System.out.print(-i+" ");
      }
      // int first_range = n-k;
      // for(int i=1; i<=first_range; i++)
      // {
      //   System.out.print(-i+" ");
      // }
      // for(int i=n-k+1; i<=n; i++)
      // {
      //   System.out.print(i+" ");
      // }
      System.out.println();
    }
  }
}
