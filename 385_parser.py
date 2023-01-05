# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if len(s)==0:
            return NestedInteger()
        if s[0]!="[":
            return NestedInteger(int(s))
        if len(s)<=2:
            return NestedInteger()
        res = NestedInteger()
        start = 1
        cnt = 0
        for i in range(1, len(s)):
            if cnt==0 and (s[i]==',' or i==len(s)-1): # 非常关键
                res.add(self.deserialize(s[start:i]))
                start = i+1
            elif s[i]=='[':
                cnt += 1
            elif s[i]==']':
                cnt -= 1
        return res