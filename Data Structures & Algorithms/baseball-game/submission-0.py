class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i=0
        score=[]
        j=0
        for i in range(len(operations)):
            if operations[i]=='+':
                score.append(int(score[j-1])+int(score[j-2]))
                j+=1
            elif operations[i]=='D':
                score.append(int(score[j-1])*2)
                j+=1
            elif operations[i]=='C':
                score.pop()
                j-=1
            else:
                score.append(int(operations[i]))
                j+=1
            print(score)
            
        return sum(score)