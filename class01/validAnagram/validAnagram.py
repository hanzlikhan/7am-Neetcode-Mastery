# valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # return sorted(s) == sorted(t)

        #using dictionary 

        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch,0)+1

        for ch in t:
            count_t[ch] = count_t.get(ch,0) + 1

        return count_s == count_t

        # using hashmap
        # if len(s) != len(t):
        #     return False
        # count = {}

        # for i in range(len(s)):    # racecar      carrace

        #     count[s[i]] = count.get(s[i],0) + 1   # r : 1  a:0

        #     count[t[i]] = count.get(t[i],0) - 1   # c : 0
        
        # for val in count.values():
        #     if val != 0:
        #         return False
        # return True
