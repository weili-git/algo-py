class Solution:

    def __init__(self, nums: List[int]):
        self.dict = defaultdict(list) # 
        for i,x in enumerate(nums):
            self.dict[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])