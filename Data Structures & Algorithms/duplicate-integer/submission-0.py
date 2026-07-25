class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        for i in s.values():
            if i%2==0:
                return True
        return False