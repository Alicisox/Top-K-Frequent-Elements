from collections import defaultdict

class Solution:

    def topKFrequent(self, nums, k):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        count = sorted(count.items(), key = lambda x: x[1])
        return [count[i][0]  for i in range(len(count)-1, len(count)-1-k, -1)]
    
    def topKFrequent_bigO_N(self, nums, k):
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        freq = [[] for _ in range(len(nums)+1)]
        for key in count.keys():
            freq[count[key]].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            if freq[i]:
                for f in freq[i]:
                    res.append(f)
                    if len(res) == k:
                        return res
        return res
    
# testing
#nums = [1,1,1,2,2,3]
#k = 2
nums = [1,1,1,1,2,2,2,2,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8]
k = 6

my_dict = Solution().topKFrequent_bigO_N(nums, k)
print(my_dict)

#nums = [1]
#k = 1

my_dict = Solution().topKFrequent(nums, k)
print(my_dict)