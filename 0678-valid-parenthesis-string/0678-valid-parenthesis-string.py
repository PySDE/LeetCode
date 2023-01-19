class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        for i, ch in enumerate(s):
            if ch == ')':
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else: 
                    return False
            elif ch == '(':
                openStack.append(i)
            else:
                starStack.append(i)
        
        while openStack and starStack:
            if openStack[-1] > starStack[-1]:
                return False
            openStack.pop()
            starStack.pop()
        
        return len(openStack) == 0