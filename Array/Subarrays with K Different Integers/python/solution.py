from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l=0
        invalid = 0
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while freq[nums[r]] == k:
                l += 1
            invalid += r - l + 1
        total = len(n) * (len(n) + 1) // 2
        return total - invalid    