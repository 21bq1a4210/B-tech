# 1. Prefix Sum

Prefix Sum involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.

### Sample Problem:
Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

### Example:

Explanation:
1. Preprocess the array A to create a prefix sum array: P = [1, 3, 6, 10, 15, 21].

2. To find the sum between indices i and j, use the formula: P[j] - P[i-1].

### LeetCode Problems:
- [Range Sum Query - Immutable (LeetCode #303)](https://leetcode.com/problems/range-sum-query-immutable/description/)


- [Contiguous Array (LeetCode #525) ](https://leetcode.com/problems/contiguous-array/description/)
    1. convert 0 to -1
    2. sum, length = 0, 0
    3. map = {0:-1}
    4. if sum in map -> l = max(l, i-map[s])
    5. else map[s] = i

    ```python
        class Solution:
        def findMaxLength(self, nums: List[int]) -> int:
            s, l = 0, 0
            m = {0:-1}
            for i in range(len(nums)):
                s += 1 if nums[i]==1 else -1
                if s in m:
                    l=max(l, i-m[s])
                else:
                    m[s]=i
            return l
    ```

- [Subarray Sum Equals K (LeetCode #560)](https://leetcode.com/problems/subarray-sum-equals-k/description/)