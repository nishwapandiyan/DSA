class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        low = max(jobs)
        high = sum(jobs)

        def canWork(limit):
            workers = [0]*k
            def dfs(index):
                if index == len(jobs):
                    return True
                for i in range(k):
                    if workers[i] + jobs[index] <= limit:
                        workers[i] += jobs[index] 

                        if dfs(index+1):
                            return True
                        workers[i] -= jobs[index]
                    if workers[i] == 0:
                        break
                return False        

                
            return dfs(0)  

        while low < high:
            mid = low+(high-low)//2
            if canWork(mid):
                high = mid
            else:
                low = mid+1   
        return low                    
