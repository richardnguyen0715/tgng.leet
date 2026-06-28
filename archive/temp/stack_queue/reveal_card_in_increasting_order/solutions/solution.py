class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        results = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if len(results) == 0:
                results.append(i)
            else:
                last = results.pop()
                results.appendleft(last)
                results.appendleft(i)
        
        return list(results)
