class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        
        ## this uses backtracking
        def find_comb(start,comb):
            
            if len(comb) == k:
                found_comb = comb[:]
                output.append(found_comb)
                return
            
            for i in range(start,n+1):
                comb.append(i)    # this is an another method to copy
                find_comb(i+1,comb)
                comb.pop()
            
        find_comb(1,[])
        
        
        
        return output
        
        
n = 4
k = 2

obj = Solution()

print(obj.combine(n,k))