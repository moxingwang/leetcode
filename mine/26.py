#!/usr/bin/python3
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow +1
                nums[slow] = nums[fast]
        

        return slow+1



data = [1,2,4,6,7,7,7,7,9]
print(Solution().removeDuplicates(data))