from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    # Greedy: Sort by units per box in descending order
        boxTypes.sort(key=lambda x: -x[1])
        
        total_units = 0
        remaining_capacity = truckSize
        
        for num_boxes, units_per_box in boxTypes:
            if remaining_capacity == 0:
                break
                
            # Take as many boxes as possible from current type
            boxes_to_take = min(num_boxes, remaining_capacity)
            
            total_units += boxes_to_take * units_per_box
            remaining_capacity -= boxes_to_take
        
        return total_units
