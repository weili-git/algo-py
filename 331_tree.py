class Solution:
    def isValidSerialization(self, preorder: str) -> bool: # why
        degree = 1 # outdegree = 1 -> root
        for node in preorder.split(","):
            if degree==0:
                return False
            if node=="#": # as leaf
                degree -= 1 # indegree = 1, outdegree = 0
            else:
                degree += 1 # indegree = 1, outdegree = 2
        return degree == 0

# 把此问题中的空节点理解成叶子节点。

# 可以理解成是节点数问题，###叶子节点数总是比非叶子节点数多一###。根据前序遍历过程，先遍历的非叶子节点数总是比叶子节点数多。

# 也可以理解为出度入度相等问题：我命名有问题，根结点的入度为0出度为2，其他非叶子结点的入度为1出度为2，叶子节点入度为1出度为0。因为根节点多出来一个出度，所以初始化度为1，一个非叶子节点时度+1，加入一个空节点（叶子节点）时度-1，如果度为0，即达到出度入度相等，已经形成一颗二叉树。

# class Solution {
# public:
#     bool isValidSerialization(string preorder) {
#         int num = 0, num1 = 0; 
#         stringstream sstr(preorder);
#         string str;
#         while (getline(sstr, str, ',')) {
#             if(num1 > num) return false;
#             if(str == "#") num1++;
#             else num++;
#         }
#         return (num1 - num) == 1;
#     }
# };

# 别的思路 从后往前，x,#,# 可以变成#，知道最后整个只有一个#