class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(list)
        counter = Counter(nums)
        
        max_freq = -1
        for num, freq in counter.items():
            bucket[freq].append(num)
            max_freq = max(max_freq, freq)
        
        results = []
        start_freq = max_freq
        
        while len(results) < k:
            if start_freq in bucket:
                results.extend(bucket[start_freq])
            start_freq -= 1
        
        return results 