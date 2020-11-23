import java.util.*;

class game{
  static void add(int[] arr, int N, int lo, int hi, int val)
  {
      arr[lo] += val;
      if (hi != N - 1)
      {
        arr[hi + 1] -= val;
      }
  }
  static void reverse(int a[], int n) 
    { 
        int[] b = new int[n]; 
        int j = n; 
        for (int i = 0; i < n; i++) { 
            b[j - 1] = a[i]; 
            j = j - 1; 
        } 
  
        /*printing the reversed array*/
        // System.out.println("Reversed array is: \n"); 
        // for (int k = 0; k < n; k++) { 
        //     System.out.println(b[k]); 
        // } 
    } 
  public static void main(String args[]) 
  {
    Scanner sc = new Scanner(System.in);
    int d, n;
    int a[], cost[]; //encoded array
    n = sc.nextInt();
    d = sc.nextInt();
    cost = new int[n];
    a = new int[n];
    for(int i=0; i<n; i++)
    {
      cost[i] = sc.nextInt();
    }
    for(int i=0; i<d; i++)
    {
      int l = sc.nextInt() - 1;
      int r = sc.nextInt() - 1;
      add(a, n, l, r, 1);
    }
    for (int i = 1; i < n; i++)
    {
      a[i] += a[i - 1];
      // System.out.print(a[i]+ " ");
    }
    // System.out.println("numbers were abobve ");
    Arrays.sort(a);
    Arrays.sort(cost);
    reverse(cost, cost.length);     
    int ans = 0;
    for(int i=0; i<n; i++)
    {
      ans += cost[i] * a[i];
    }
    System.out.println(ans);
  }
}
