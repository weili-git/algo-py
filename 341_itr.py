# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ptr = nestedList, 0
        self.stack = []
    
    def next(self) -> int:
        if not self.hasNext():
            return None

        arr, idx = self.ptr
        res = arr[idx].getInteger()
        self.ptr = (arr, idx + 1)
        return res
    
    def hasNext(self) -> bool:
         while True:
            arr, idx = self.ptr
            if idx >= len(arr):
                if not self.stack:
                    return False
                self.ptr = self.stack.pop() # until integer
                continue
            if arr[idx].isInteger():
                return True
            self.stack.append((arr, idx+1))
            self.ptr = (arr[idx].getList(), 0)



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())