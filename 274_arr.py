class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h-index means [h] paper cites >= h, and [n - h] cites < h
        citations.sort()
        for idx, cite in enumerate(citations):
            h = len(citations) - idx  # 
            if h <= cite:
                return h
        return 0