// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

// Example 1:
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

#include <bits/stdc++.h>
using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    int m = nums2.size();
    if (n > m) return findMedianSortedArrays(nums2, nums1);

    int imin = 0, imax = n, halfLen = (n + m + 1) / 2;  
    while (imin <= imax) {
        int i = (imin + imax) / 2;
        int j = halfLen - i;

        if (i < n && j > 0 && nums2[j-1] > nums1[i]) {
            imin = i + 1;  
        }
        else if (i > 0 && j < m && nums1[i-1] > nums2[j]) {
            // i is too big, must decrease it
            imax = i - 1;
        }
        else {
            int maxLeft = 0;
            if (i == 0) maxLeft = nums2[j-1];
            else if (j == 0) maxLeft = nums1[i-1];
            else maxLeft = max(nums1[i-1], nums2[j-1]);

            if ((n + m) % 2 == 1) return maxLeft;

            int minRight = 0;
            if (i == n) minRight = nums2[j];
            else if (j == m) minRight = nums1[i];
            else minRight = min(nums1[i], nums2[j]);

            return (maxLeft + minRight) / 2.0;
        }
    }
    return 0.0;
}

int main() {
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    cout << findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}

