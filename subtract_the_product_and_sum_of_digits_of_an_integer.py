from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
    	# List of digits in n
        nums = [int(x) for x in str(n)]
        # Substract sum of digits from product
        return reduce((lambda x,y: x*y), nums) - sum(nums)