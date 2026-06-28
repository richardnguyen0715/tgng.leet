class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction = 0
        
        # Simulate at most 4 cycles
        for _ in range(4):
            for instruction in instructions:
                if instruction == 'G':
                    dx, dy = directions[direction]
                    x, y = x + dx, y + dy
                elif instruction == 'L':
                    direction = (direction - 1) % 4
                elif instruction == 'R':
                    direction = (direction + 1) % 4
            
            # If back to origin, it's bounded
            if x == 0 and y == 0:
                return True
        
        # After 4 cycles, if not at origin, it's unbounded
        return False