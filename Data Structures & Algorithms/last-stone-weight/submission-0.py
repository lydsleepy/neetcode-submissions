class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            
            one = heapq.heappop(maxHeap)
            two = heapq.heappop(maxHeap)
            
            if one < two: # negative numbers
                heapq.heappush(maxHeap, one - two)
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        elif len(maxHeap) == 0:
            return 0