# For this I took the approach to subtract from the target and see if the remainder is present in the list
# This removes the need to check every pair and add them together

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = []
        item = 0

        for x in range(0, len(numbers)):
            if len(nums) > 0:
                break

            else:
                item = target - numbers[x]

                for y in range(1, len(numbers)):
                    
                    if y != x:
                        
                        if item == numbers[y]:
                            nums.append(x)
                            nums.append(y)
                            break

        return nums
