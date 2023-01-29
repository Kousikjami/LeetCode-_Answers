class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=max(candies)
        new=[True]*len(candies)
        for i in range(0,len(candies)):
            candies[i]=candies[i]+extraCandies
            if candies[i]>=n:
                new[i]=(True)
            else:
                new[i]=(False)
        return new