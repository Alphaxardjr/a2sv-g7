from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while True:
                # check if prefix is longer then reduce the last element
                if len(prefix)>len(s):
                    prefix = prefix[:-1]
                    continue
                
                # check if each characters match
                matches = True
                for i in range(len(prefix)):
                    if prefix[i] !=s[i]:
                        matches = False
                        break
                
                # if it matches then break and return the prefix else shrink the last char
                if matches:
                    break
                else:
                    prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
