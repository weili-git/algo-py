class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                # 寻找环的入口位置
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]

# 1, 2, [3], 4, 5, [3]

# 2, [9], 1, 5, 3, 6, 8, 7, [9]
# 2, [9], 1, 5, 3, 6, 8, 7  (slow)
# [9], 5, 6, 7, 1, 3, 6, 7  (fast)



# proof
# 1,2,3,x,[11], 22, 33, ..., y
#          a (x)
#                        b (2x)
# b再走2y-2x相遇
# 当a到达入口时，b所在位置(2y+1)%y => 1，与a在入口相遇