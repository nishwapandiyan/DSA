class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low+(high-low)//2

            req_days = 1
            curr = 0

            for weight in weights:
                if curr+weight > mid:
                    req_days += 1
                    curr = weight
                else:
                    curr += weight
            if req_days <= days:
                high = mid
            else:
                low = mid+1
        return low                            