class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        sortedCards = sorted(count.keys())

        groupStartQueue = deque()
        openGroups = 0
        lastCard = -1

        for currentCard in sortedCards:
            if (openGroups > 0 and currentCard > lastCard + 1) or openGroups > count[currentCard]:
                return False
            
            groupStartQueue.append(count[currentCard] - openGroups)
            lastCard = currentCard
            openGroups = count[currentCard]

            if len(groupStartQueue) == groupSize:
                openGroups -= groupStartQueue.popleft()
            
        return openGroups == 0
