class Solution:
    def isValid(self, s: str) -> bool:
        try:
            if not s:
                return False
            else:
                #Empty stack
                stack=[]
                d={'(':')','{':'}','[':']'}
                for item in s:
                    if item in d.keys():
                        stack.append(item)
                    elif len(stack)>0 and d.get(stack[-1])==item:
                        stack.pop()
                    else:
                        return False
                return len(stack)==0

        except Exception as e:
            print(e)






        