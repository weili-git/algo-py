from collections import defaultdict
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        sum2pair = defaultdict(lambda: [])
        for i in range(m):
            for j in range(n):
                s = nums1[i]+nums2[j]
                sum2pair[s] = sum2pair[s] + [[nums1[i], nums2[j]]]
        
        sort_sum = [i for i in sum2pair.keys()]
        heapq.heapify(sort_sum)
        left = k
        res = []
        while left>0:
            pairs = heapq.heappop(sort_sum)
            pairs = sum2pair[pairs]
            if len(pairs) > left:
                res += pairs[:left]
                return res
            res += pairs
            left -= len(pairs)
        return res

# 16 min timeout, O(m*n + k)

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        if k==m*n:
            return [[nums1[i], nums2[j]] for i in range(m) for j in range(n)]
        
        vis = [[0 for i in range(n)] for j in range(m)]
        res = []
        heap = [nums1[0]+nums2[0]]
        sum2pair = defaultdict(lambda: [])
        sum2pair[nums1[0]+nums2[0]] = [[0, 0]] # index

        def check_corner(x, y):
            if x-1<0 or y-1<0: # border
                return True
            if vis[x-1][y] and vis[x][y-1]:
                return True
            
        while k>0:
            sum = heapq.heappop(heap)
            i, j = sum2pair[sum].pop(0)
            res.append([nums1[i], nums2[j]])
            vis[i][j] = 1
            if j+1<n and check_corner(i, j+1):
                heapq.heappush(heap, nums1[i]+nums2[j+1])
                sum2pair[nums1[i]+nums2[j+1]].append([i, j+1])

            if i+1<m and check_corner(i+1, j):
                heapq.heappush(heap, nums1[i+1]+nums2[j])
                sum2pair[nums1[i+1]+nums2[j]].append([i+1, j])
            k -= 1
        return res
        
# 25 min, O(k^2)

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))] # 相当于已经建好了堆，不需要执行heapify
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
    
# similar 固定只向右边移动




        # [u_m, v_n] <= [u_m+1, v_n]
        # [u_1, v_1] smallest
        # [u_1, v_2], [u_2, v_1]
        # bigger one, [u_1, v_3], [u_2, v_3], [u_3, v_1], [u_3, v_2]

        # [ ] [1] [2] [3] [4]
        # [1] [1] [1] [1] [1]
        # [2] [1] [1] [1] [1]
        # [3] [1] [1] [1] [1]
        # [4] [1] [1] [1] [1]
        # [5] [1] [1] [1] [1]

        # smallest in the left corner

        # [0, 0] 
        # [0, 1]
        # [1, 0]

        # [i, j] is picked as smallest
        # [i, j+1], [i+1, j] appended if not vis

