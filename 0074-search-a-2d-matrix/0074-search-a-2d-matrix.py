class Solution:
    def searchMatrix(self, mat: List[List[int]], item: int) -> bool:
        
        r=len(mat)
        c=len(mat[0])
        low=0
        high=r*c-1
        while low<=high:
            
            mid=(low+high)//2
            row=mid//c
            column=mid%c
            if mat[row][column]==item:
                
                return True
            elif mat[row][column]<item:
                low=mid+1
            else:
                high=mid-1
        return False