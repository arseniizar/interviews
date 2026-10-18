"""
LeetCode 33: Search in Rotated Sorted Array (Medium)
Time: O(log n), Space: O(1)

C++ Solution:
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            // Left half is sorted
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            // Right half is sorted
            else {
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }

        return -1;
    }
};
```
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print("Test 1 ([4,5,6,7,0,1,2], target=0):", sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print("Test 2 ([4,5,6,7,0,1,2], target=3):", sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print("Test 3 ([1], target=0):", sol.search([1], 0))                                  # -1
