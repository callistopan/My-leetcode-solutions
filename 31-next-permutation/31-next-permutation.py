class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inversion_point= len(arr)-2
        while inversion_point>=0 and arr[inversion_point]>=arr[inversion_point+1]:
            inversion_point-=1


        if inversion_point==-1:
            arr.sort()
            return

        # swap the smallest entry after the inversion point
        # that is greater than the inversion point
        # use binary search
        # find the smallest entry after the inversion point

        for i in range(len(arr)-1,inversion_point,-1):
            if arr[i]>arr[inversion_point]:
                arr[i],arr[inversion_point]=arr[inversion_point],arr[i]
                break

        # reverse the array after the inversion point
        l=inversion_point+1
        r=len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1