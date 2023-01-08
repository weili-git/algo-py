class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            if i<2 or num>nums[i-2]: # 因为是（非递减数组）！，我们只需要判断左边第二个元素是否相同就行
                nums[i] = num
                i += 1
        return i