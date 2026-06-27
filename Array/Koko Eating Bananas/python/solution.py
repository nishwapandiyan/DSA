class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)

        while low < high:
            mid = low + (high - low)//2

            hours = 0

            for pile in piles:
                hours += (pile + mid-1) // mid

            if hours <= h:
                high = mid
            else:
                low = mid+1
        return low                