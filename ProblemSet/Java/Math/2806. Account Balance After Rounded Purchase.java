class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        /*
        int res;
        int a = purchaseAmount / 10;
        int b = a + 1;
        int tot = 100;
        if(purchaseAmount - a * 10 < b * 10 - purchaseAmount){
            res = tot - a * 10;
        }
        else{
            res = tot - b * 10; // two condiction
        }
        return res;
        */
        return 100-(purchaseAmount%10 >= 5 ?(purchaseAmount/10+1)*10 : (purchaseAmount/10)*10); 
    }
}