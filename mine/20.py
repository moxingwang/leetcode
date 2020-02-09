#!/usr/bin/python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        smap={
            '(':')',
            '{':'}',
            '[':']',
        }

        #遍历字符串
        for x in s:
            if x in smap:
                stack.append(smap[x])
            else:
                if len(stack) != 0:
                    top_ele = stack.pop()
                    if x != top_ele:
                        return False
                    else:
                        continue
                else:
                    return False
        
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid('{[}'))