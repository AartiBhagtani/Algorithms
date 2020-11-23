https://www.hackerrank.com/challenges/30-binary-numbers/problem
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String binary_s = Integer.toBinaryString(n);
        //convert to binary
        String[] strparts = binary_s.split("0");
        //above we get all strings of ones, below find max from them
        //can check #System.out.println(Arrays.toString(strparts));
        int count = 0;
        for(int i=0;i<strparts.length;i++)
        {
            if(count<strparts[i].length())
            {
                count = strparts[i].length();
            }
        }
        System.out.print(count);
    }
}
