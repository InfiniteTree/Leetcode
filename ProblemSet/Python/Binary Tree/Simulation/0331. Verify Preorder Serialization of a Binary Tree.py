class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        order = preorder.split(",")
        #stack = []
        '''
        cnt = 1 # count the remained place
        for node in order:
            if stack:
                stack.pop()
                cnt += 2
            if node.isdigit():
                stack.append(node)
                cnt -= 1
            elif node == "#":
                cnt -= 1
            if cnt < 0:
                return False
        return True if len(stack) == 0 and cnt == 0 else False
        '''
        '''
        # Method 1. Using stack
        
        for node in order:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3].isdigit():
                for _ in range(3):
                    stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack.pop() == "#"
        '''
        # Method 2. Cnt in and out degree
        cnt = 1
        for node in order:
            cnt -= 1
            if cnt < 0:
                return False
            if node.isdigit():
                cnt += 2
        return cnt == 0


            
                


