class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # pop one asteroids
        # add array 'tmp'
        # while asteroids still have asteroids:
        # pop one asteroid
        # if popped is positive and the last asteroid in tmp is negative, keep the one with higher val
        # if popped is negative, add popped to 'tmp'

        res = [asteroids.pop()]
        while asteroids:
            pop = asteroids.pop()
            if pop > 0:
                while res and res[-1] < 0 and -res[-1] < pop:  # pop smaller ateroids going left
                    print("f")
                    res.pop()
                
                if res and res[-1] < 0 and -res[-1] == pop:  # two asteroids have the same size
                    res.pop()
                    continue
                
                if not res or res[-1] > 0:  # Add positive asteroid when no asteroid goes left
                    res.append(pop)
            else:
                res.append(pop)

        return res[::-1]
