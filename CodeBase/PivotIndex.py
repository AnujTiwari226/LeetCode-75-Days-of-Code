from typing import List


class Solution:

    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        """
        initialize left = 0 and right = sum of all the numbers in the list nums -
            using either sum() or a loop to get total
        1.
        Iterate through the list from 0 to len(nums)-1 and compare values l and right-nums[i]

        :param nums: array of integers
        :return: Return the leftmost pivot index. If no such index exists, return -1.
        """
        left, right = 0, 0
        for item in nums:
            right += item
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


if __name__ == '__main__':
    """
    Given an array of integers nums, calculate the pivot index of this array.
        The pivot index is the index where the sum of all the numbers 
        strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
        
    """

    sol = Solution
    print('input - ')
    nums = list(map(int, input().split()))
    print(sol.pivotIndex(nums=nums))
