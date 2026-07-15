class MaxNumberFinder:
    def __init__(self, nums):
        # your code here
        self.nums=nums
        

    def find_max_number(self):
        # your code here
        if not self.nums:
            return None
        
        return max(self.nums)

finder = MaxNumberFinder([1,3,6])
print(finder.find_max_number())
        