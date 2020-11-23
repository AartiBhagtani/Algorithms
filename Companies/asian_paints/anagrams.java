import java.util.*;

class anagrams{
    public static void main(String args[]) 
    {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.next();
        String s2 = sc.next();
        
        if(s1.length() != s2.length())
        {
            System.out.println("false");
        }

        else
        {
            HashMap<Character, Integer> hmap1 = new HashMap<>(); 
            HashMap<Character, Integer> hmap2 = new HashMap<>(); 

            for (int i = 0; i < s1.length(); i++)
            {
                char element = s1.charAt(i);
                if (hmap1.get(element) == null){ 
                    hmap1.put(element, 1); 
                } 
                else{ 
                    Integer c = (int)hmap1.get(element); 
                    hmap1.put(element, ++c); 
                } 
            }

            for (int i = 0; i < s2.length(); i++)
            {
                char element = s2.charAt(i);
                if (hmap2.get(element) == null){ 
                    hmap2.put(element, 1); 
                } 
                else{ 
                    Integer c = (int)hmap2.get(element); 
                    hmap2.put(element, ++c); 
                }
            }

            if (hmap1.equals(hmap2)){
                System.out.println("true");
            }
            else
            {
                System.out.println("false");
            }
        }
    }
}