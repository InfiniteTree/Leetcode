import java.util.*;

class Solution {
    public int romanToInt(String s) {
        int ans = 0;
        int i = 1;
        int cur = getValue(s.charAt(0));
        while (i <= s.length()-1){
            int post = getValue(s.charAt(i));
            if (cur >= post){
                ans += cur;
            }
            else{
                ans -= cur;
            }
            i++;
            cur = post;
        }
        ans += cur;
        return ans;
    }

    private int getValue(char ch) {
        switch(ch) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;

        }
    }
}