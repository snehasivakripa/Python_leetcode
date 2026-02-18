from typing import List


class contains_duplicate:
    #Brute Force
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]==nums[j]:
    #                 return True
    #     return False

    #Sorting
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(1,len(nums)):
    #         if nums[i]==nums[i-1]:
    #             return True
    #     return False

    #Hashset
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

obj=contains_duplicate()
result=obj.hasDuplicate([1,2,3,2,4])
print(result)
