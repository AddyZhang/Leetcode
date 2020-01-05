class Solution:
    def isValid(self, s: str) -> bool:
        strlist = list(s)
        stack = []
        
        if len(strlist) % 2 != 0:
            print(1)
            return False 
        m = len(strlist)//2
        print(m)
        for x in strlist:
            if x == '(' or x == '[' or x == '{':
                if x == '(':
                    stack.append(')')
                elif x == '[':
                    stack.append(']')
                elif x == '{':
                    stack.append('}')
            if x == ')' or x == ']' or x == '}':
                if len(stack) != 0:
                    val = stack[-1]
                    if val == x:
                        stack.pop()
            
        return True if len(stack) == 0 else False
