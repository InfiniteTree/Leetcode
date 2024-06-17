class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String str = s + s; // str = s1 + s2 + s1 + s2
        return str.substring(1, str.length()-1).contains(s); // str = s3 + s2 + s1 + s4 => judge whether s2 == s1, if yes, it contatins s because s2+s1 = s1+s2 
    }
}