class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokenMaps = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenMaps:
            return
        self.tokenMaps[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokenMaps:
            return
        if self.tokenMaps[tokenId] <= currentTime:
            return
        
        self.tokenMaps[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for expireTime in self.tokenMaps.values():
            if expireTime > currentTime:
                count += 1
        
        return count

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)