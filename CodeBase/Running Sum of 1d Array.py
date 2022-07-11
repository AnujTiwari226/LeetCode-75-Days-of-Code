from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        sum = 0
        for item in nums:
            sum += item
            result.append(sum)
        return result

    @staticmethod
    def running_sum_1(nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


if __name__ == "__main__":
    print("Enter list of values - ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print("Using sep list to get sum : ", sol.runningSum(nums))
    print("Using same list: ", sol.running_sum_1(nums))
