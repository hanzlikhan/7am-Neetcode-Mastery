# contains duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  return (len(nums) != len(set(nums))) 
        Set = set(nums)  # create a set and add all values 

        # len -> 5    set -> 4 
        return len(Set) != len(nums)
        
        # time complexity = O(n)
          # create set 

        # for n in nums:
        #     if n not in Set:
        #         Set.add(n)
        
        # if len(Set) != len(nums):
        #     return True
        # return False 