class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[mid]
            

        [1, 2, 3, 4, 5, 6, 7]
        [4, 5, 6, 0, 1, 2, 3]
        [4, 5, 6, 7, 0, 1, 2]
        [5, 6, 0, 1, 2, 3, 4]


        # looking at array
        # if a smaller element is found to the right; this means min is between current element and that element
        # if a larger element is found to the right; this means min is between that element and end of search space