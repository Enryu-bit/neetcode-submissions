class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size() , m = nums2.size() , picking = (n + m) / 2 + (n + m) % 2;
        if(n > m) return findMedianSortedArrays(nums2 , nums1);
        // auto helper = [&](int mid) {
            

        //     if(l1 <= )
        // }

        int low = 0 , high = n;
        while(low <= high){
            int mid = low + (high - low)/2;
            
            double mid2 = picking - mid;
            double l1 = (mid ? nums1[mid - 1] : INT_MIN);
            double r1 = (mid != n ? nums1[mid] : INT_MAX);
            double l2 = (mid2 ? nums2[mid2 - 1] : INT_MIN);
            double r2 = (mid2 != m ? nums2[mid2] : INT_MAX);

            if(l1 <= r2 && l2 <= r1) {
                if((n + m) % 2)return max(l1 , l2);
                return (max(l1 , l2) + min(r1 , r2)) / 2.0;
            }
            else if(l1 > r2) high = mid - 1;
            else low = mid + 1;
        }
        return 0;
    }
};
