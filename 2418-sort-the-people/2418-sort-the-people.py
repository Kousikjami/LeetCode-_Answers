class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res=[]
        for i in range(len(heights)):
            res.append([heights[i],names[i]])
        res.sort(reverse=True)
        k=[]
        for i in res:
            k.append(i[1])
        return k