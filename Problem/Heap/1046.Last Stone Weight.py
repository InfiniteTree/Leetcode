class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones] # Change the Min heap in Python to a Max heap
        heapq.heapify(heap)

        while (len(heap)>1):
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            if a - b != 0:
                heapq.heappush(heap, a-b)

        return -heap[0] if heap else 0
    