from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        '''
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        print(mp)
        return list(mp.values())
        '''
        # Method 2 Hash Num list
        for st in strs:
            cnt = [0] * 26 
            for ch in st:
                cnt[ord(ch) - ord("a")] += 1
            #print(tuple(key))
            mp[tuple(cnt)].append(st) # cnt is the key and st is the value
        return list(mp.values())
