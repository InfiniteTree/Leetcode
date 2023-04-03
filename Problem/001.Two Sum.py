class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        '''
        # Use a hash table map to record the orgal indices
        nums_map = [(idx,val) for idx,val in enumerate(nums)]
        nums_map.sort(key=lambda x: x[1])
        op1_idx, op2_idx = 0, len(nums)-1
        while op1_idx<op2_idx:
            cur_sum = nums_map[op1_idx][1] + nums_map[op2_idx][1]
            if cur_sum == target:
                return [nums_map[op1_idx][0], nums_map[op2_idx][0]]
            
            elif cur_sum < target: # need to increase the cur_sum
                op1_idx += 1
            else:
                op2_idx -= 1 # # need to decrease the cur_sum

            # pass

