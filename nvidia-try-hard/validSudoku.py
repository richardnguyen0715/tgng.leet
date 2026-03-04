from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            seen = set()
            for cell in row:
                if cell != '.' and cell in seen:
                    return False
                if cell != '.':
                    seen.add(cell)
        
        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell != '.' and cell in seen:
                    return False
                if cell != '.':
                    seen.add(cell)
        
        # Check 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        cell = board[row][col]
                        if cell != '.' and cell in seen:
                            return False
                        if cell != '.':
                            seen.add(cell)
        
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                
                if cell == '.':
                    continue
                
                # Calculate box index: box = (row // 3) * 3 + (col // 3)
                box_index = (row // 3) * 3 + (col // 3)
                
                # Check if number already exists
                if (cell in rows[row] or 
                    cell in cols[col] or 
                    cell in boxes[box_index]):
                    return False
                
                # Add to tracking sets
                rows[row].add(cell)
                cols[col].add(cell)
                boxes[box_index].add(cell)
        
        return True
    
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use bitmasks instead of sets (more memory efficient)
        rows = [0] * 9
        cols = [0] * 9  
        boxes = [0] * 9
        
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                
                if cell == '.':
                    continue
                
                # Convert '1'-'9' to bit position 0-8
                bit = 1 << (int(cell) - 1)
                box_index = (row // 3) * 3 + (col // 3)
                
                # Check if bit already set
                if (rows[row] & bit or 
                    cols[col] & bit or 
                    boxes[box_index] & bit):
                    return False
                
                # Set the bit
                rows[row] |= bit
                cols[col] |= bit
                boxes[box_index] |= bit
        
        return True
    
    

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                
                if cell != '.':
                    # Create unique identifiers for each constraint
                    row_key = f"row{row}-{cell}"
                    col_key = f"col{col}-{cell}"  
                    box_key = f"box{row//3}{col//3}-{cell}"
                    
                    # Check if any constraint violated
                    if (row_key in seen or 
                        col_key in seen or 
                        box_key in seen):
                        return False
                    
                    # Add all constraints
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        
        return True
    

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        three = defaultdict(set)

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != ".":
                    grid = (i // 3) * 3 + j // 3
                    if x in row[i] or x in col[j] or x in three[grid]:
                        return False
                    row[i].add(x)
                    col[j].add(x)
                    three[grid].add(x)
            
        return True