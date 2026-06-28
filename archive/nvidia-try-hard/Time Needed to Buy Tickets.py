from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        # Queue stores (person_index, remaining_tickets)
        queue = deque((i, tickets[i]) for i in range(n))
        
        time = 0
        
        while queue:
            person_idx, remaining = queue.popleft()
            
            # This person buys 1 ticket
            time += 1
            remaining -= 1
            
            # Check if person k is done
            if person_idx == k and remaining == 0:
                return time
            
            # If they still need more tickets, go to back of queue
            if remaining > 0:
                queue.append((person_idx, remaining))
        
        return time  # Should never reach here if input is valid