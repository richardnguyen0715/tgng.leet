from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = {"circular":0, "squre":0}
        for student in students:
            if student ==0:
                cnt["circular"]+=1
            else:
                cnt["squre"]+=1
        
        for sandwiche in sandwiches:
            if sandwiche ==0:
                if cnt["circular"]==0:
                    break
                cnt["circular"]-=1
            else:
                if cnt["squre"] ==0:
                    break
                cnt["squre"]-=1
        return cnt["circular"]+ cnt["squre"]
            



        