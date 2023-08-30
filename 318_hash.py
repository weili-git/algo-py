class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def get_hash(str):
            hash_value = 0
            for i in range(26):
                if str.find(chr(97+i)) != -1:
                    hash_value += 1
                hash_value <<= 1
            return hash_value
        arr = [get_hash(word) for word in words]
        n = len(words)
        maxProduct = 0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] & arr[j]==0:
                    maxProduct = max(maxProduct, len(words[i])*len(words[j]))
        return maxProduct
