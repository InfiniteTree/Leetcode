# Min-Heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #count = 0
        my_heap = nums[0:k]
        heapq.heapify(my_heap)
        # remain the largest k element in a quque
        for i in range(k, len(nums)):
            min =  my_heap[0]
            if nums[i] > min:
                heapq.heappop(my_heap)
                heapq.heappush(my_heap, nums[i])
        return my_heap[0]
        