from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        size = len(nums)
        nums.sort()

        for x in range(size):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            start = x + 1
            end = size - 1

            while start < end:
                total = nums[x] + nums[start] + nums[end]

                if total == 0:
                    ans.append([nums[x], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                elif total < 0:
                    start += 1
                else:
                    end -= 1

        return ans


# Driver code
obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(obj.threeSum(nums))

