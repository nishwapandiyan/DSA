class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if len(s) <= 1:
            return -1
        return len(s[k:len(s)-k])    