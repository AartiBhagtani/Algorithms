public class test{
    
    public static void main(String args[]) 
    {
        final String s1 = "all men : 4";
        final String s2 = "all men : "+s1.length();

        System.out.println("all men are " + s1 == s2);
    }

}

// Answer
// option b - "All men are equal : false"

// since string man1 and man2 are different 
// man1 = "All men are equal : 27"
// man2 = "All men are equal : 29"
