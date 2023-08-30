class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self.build(nums, 0, 0, self.n-1)

    def build(self, nums, node, s, e):
        # index 0 as root
        if s==e: # leaf node
            self.tree[node] = nums[s]
            return
        m = s + (e-s)//2
        self.build(nums, node*2+1, s, m) # left subtree
        self.build(nums, node*2+2, m+1, e) # right subtree
        self.tree[node] = self.tree[node*2+1] + self.tree[node*2+2]

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n-1)

    def change(self, index, val, node, s, e):
        if s==e:
            self.tree[node] = val
            return
        m = s + (e-s)//2
        if index <= m:
            self.change(index, val, node*2+1, s, m)
        else:
            self.change(index, val, node*2+2, m+1, e)
        self.tree[node] = self.tree[node*2+1] + self.tree[node*2+2]

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n-1)

    def range(self, left, right, node, s, e):
        if left==s and right==e:
            return self.tree[node]
        m = s + (e-s)//2
        if right<=m:
            return self.range(left, right, node*2+1, s, m)
        if left > m:
            return self.range(left, right, node*2+2, m+1, e)
        return self.range(left, m, node*2+1, s, m) + self.range(m+1, right, node*2+2, m+1, e)