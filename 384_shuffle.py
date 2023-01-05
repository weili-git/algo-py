import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.permutation = [i for i in range(len(nums))]

    def reset(self) -> List[int]:
        # self.permutation = [i for i in range(len(self.nums))]
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.permutation)
        return [self.nums[i] for i in self.permutation]


    def shuffle_(self): # 
        tmp = self.nums
        for i in range(1, len(self.nums)):
            r = random.randint(i+1)
            if r!=i:
                tmp[i], tmp[r] = tmp[r], tmp[i]
        return tmp