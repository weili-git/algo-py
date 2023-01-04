class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TreeNode(-1)

        for num in nums: # build the binary tree
            cur_node = root
            for i in range(32):
                if num & (1<<(31-i)) == 0:
                    if not cur_node.left:
                        cur_node.left = TreeNode(0)
                    cur_node = cur_node.left
                else:
                    if not cur_node.right:
                        cur_node.right = TreeNode(1)
                    cur_node = cur_node.right
            cur_node.left = TreeNode(num)

        res = 0
        for num in nums:
            cur_node = root
            # 有路一定能走到叶子节点
            for i in range(32):
                if num & (1<<(31-i)) == 0:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node = cur_node.right
            tmp = cur_node.left.val
            res = max(res, num^tmp)
        return res

