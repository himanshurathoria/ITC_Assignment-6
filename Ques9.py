class solution:
    def validity(self,str1):
        accumulate=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accumulate.append(i)
            elif len(accumulate)==0 or parentheses[accumulate.pop()]!=i:
                return False
        return len(accumulate)==0
print(solution().validity("[)"))