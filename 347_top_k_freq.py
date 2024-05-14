from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(lambda: 0)
        for n in nums:
            cnt[n] = cnt[n] + 1
        res = []
        for elem in cnt.keys():
            print(res)
            n = len(res)
            if n==0:
                res.append(elem)
            elif n<k:
                for i in range(n):
                    if cnt[elem]>=cnt[res[i]]:
                        res.append(0) # increase the len of res
                        for j in range(n-i): # move n-i numbers and put elem
                            res[n-j] = res[n-j-1] # new len of res is n+1, last idx is n
                        res[i] = elem
                        break
                if len(res)==n:
                    res.append(elem) # the minimum one, dont forget
            else: # n==k
                for i in range(k):
                    if cnt[elem]>=cnt[res[i]]:
                        for j in range(k-i-1): # move k-i-1
                            res[k-j-1] = res[n-j-2]
                        res[i] = elem
                        break
        return res
        # 34 min

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(lambda: 0)
        for n in nums:
            cnt[n] = cnt[n] + 1
        heap = []
        for num, freq in cnt.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq, num)) # O(nlogk) 总共
            else:
                if freq > heap[0][0]: # freq of minimum
                    heapq.heappushpop(heap, (freq, num))
        res = [num for freq, num in heap]
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter, heap
        cnter = Counter(nums)
        cnter_heap = [(-v, k) for k, v in cnter.items()] # O(n)，自底向上建堆效率更高
        heapq.heapify(cnter_heap)
        return [heapq.heappop(cnter_heap)[1] for i in range(k)]