# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, e in enumerate(nums):
            if e in store:
                return [store[e], i]
            tmp = target - e
            store[tmp] = i
