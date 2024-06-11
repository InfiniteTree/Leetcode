import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int l_ptr = 0;
        int r_ptr = people.length-1;
        int ctn = limit; //container
        int p = 2; //2 seat in a boat for the passengers
        int res = 1;
        while (l_ptr <= r_ptr){
            if(ctn < people[l_ptr] || p == 0){
                res++; //Add a new boat
                p = 2;
                ctn = limit;
                continue;
            }
            else if (ctn >= people[r_ptr]){
                ctn -= people[r_ptr];
                r_ptr--;
                p--;
                continue;
            }
            else if (ctn >= people[l_ptr]){
                ctn -= people[l_ptr];
                p--;
                l_ptr++;
            }
        }
        return res;
    }
}