class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):  # check with right neighbor
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        print(candies)
        
        for i in range(len(ratings) - 2, -1, -1): # check with left neighbor
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        print(candies)
        
        return sum(candies)
