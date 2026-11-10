class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Sorting counts solution 
        count = {} ## Create a hashmap with num -> count pairs

        for num in nums:  ## iterate through the numbers
            count[num] = 1 + count.get(num, 0) ##updating the value of the num pairs

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
