class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans = 0 , n = nums.size();
        for(int i = 0 ; i < 32 ; i++){
            int count = 0;
            for(int j = 0 ; j<n ; j++){
                if((1<<i) & (nums[j]))count++;
            }
            cout<<count<<" "<<(1<<i)<<endl;
            if(count > (n / 2)) ans = ans | (1<<i);
        }
        return ans;
    }
};