import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=defaultdict(int)
        total=0
        res=0
        left=0
        for r in fruits:
            count[r]+=1
            total+=1
            while len(count)>2:
                f=fruits[left]
                count[f]-=1
                total-=1
                
                left+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,total)
        return res