class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        give = 1
        while True:
            if candies <= 0:
                break
            
            for i in range(len(res)):
                
                if candies - give < 0:
                    res[i] += candies
                    return res
                
                candies -= give
                res[i] += give
                give += 1
        
        return res
