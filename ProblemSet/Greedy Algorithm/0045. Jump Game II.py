class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        max_reachable = 0
        end_bound = 0 # point to the index that has jumped
        if n == 1:
            return step

        for i in range(n-1):
            max_reachable = max(max_reachable, i + nums[i])
            if i==end_bound:
                end_bound = max_reachable
                step += 1
        return step
    
        '''
        ptr = 0
        hold = nums[ptr]
        step = 0
        while ptr < len(nums)-1:
            farthest = hold + ptr
            if farthest < len(nums)-1: # Jump to the place with maximum length of a jump + largest idx
                for i in range(ptr+1, ptr+hold+1):
                    temp = i + nums[i]
                    if temp >= farthest:
                        farthest = temp
                        max_i = i
                ptr = max_i
                hold = nums[ptr]
                
            else:
                ptr = farthest
            #print(ptr, hold)
            step += 1
        return step
        '''
    

        