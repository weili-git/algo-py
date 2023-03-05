class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        i, j = 0, n-1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] < nums[i]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] == nums[i]:
                i += 1
        return False
# 该题与33. 搜索旋转排序数组的区别在于，这题的数组中可能会出现重复元素。二分查找的本质就是在循环的每一步中考虑排除掉哪些元素，本题在用二分查找时，只有在nums[mid]严格大于或小于左边界时才能判断它左边或右边是升序的，这时可以再根据nums[mid], target与左右边界的大小关系排除掉一半的元素；当nums[mid]等于左边界时，无法判断是mid的左边还是右边是升序数组，而只能肯定左边界不等于target（因为nums[mid] != target），所以只能排除掉这一个元素，让左边界加一。