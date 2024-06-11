class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #people.sort(reverse=True, key=lambda x:(x[0],-x[1]))
        people.sort(key=lambda x:(-x[0],x[1]))
        ret = []
        for x in people:
            ret.insert(x[1],x)
        return ret
