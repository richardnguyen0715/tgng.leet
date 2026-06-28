from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Ý tưởng: mỗi con nói có K con khác cùng màu với nó -> một nhóm cùng màu ít nhất phải có K + 1 con. -> tính số lượng group tối thiểu để chứa đủ freq con nói * số lượng mỗi group
        
        from collections import Counter
        
        count = Counter(answers)
        total = 0
        
        for answer, freq in count.items():
            group_size = answer + 1
            # Ceiling division: (a + b - 1) // b
            num_groups = (freq + group_size - 1) // group_size
            total += num_groups * group_size
        
        return total