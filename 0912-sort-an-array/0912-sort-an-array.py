class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)
        return nums 
      
        
    def merge_sort(self,arr, l, r):
        if l < r:   #if l is less than r, divide array into two halves
            m = (l+r)//2    #m is midpoint
            self.merge_sort(arr, l, m)   #sort left half
            self.merge_sort(arr, m+1, r) #sort right half
            self.merge(arr, l, m, r)    #merge two sorted halves

    def merge(self,arr, l, m, r):    #merge two sorted halves
        n1 = m - l + 1  #n1 is length of left half
        n2 = r - m   #n2 is length of right half
        L = [0]*(n1)    #create left half array
        R = [0]*(n2)    #create right half array
        for i in range(0, n1):  #copy left half to left half array
            L[i] = arr[l + i]   #copy left half to left half array
        for j in range(0, n2):  #copy right half to right half array
            R[j] = arr[m + 1 + j]   #copy right half to right half array
        i = 0   #i is index of left half
        j = 0   #j is index of right half
        k = l   #k is index of merged array
        while i < n1 and j < n2:    #while i and j are less than n1 and n2
            if L[i] <= R[j]:    #if left element is less than or equal to right element
                arr[k] = L[i]   #copy left element to merged array
                i += 1  #increment i    
            else:        #if left element is greater than right element
                arr[k] = R[j]   #copy right element to merged array
                j += 1  #increment j
            k += 1  #increment k
        while i < n1:   #while i is less than n1
            arr[k] = L[i]   #copy left element to merged array
            i += 1  #increment i
            k += 1  #increment k
        while j < n2:   #while j is less than n2
            arr[k] = R[j]   #copy right element to merged array
            j += 1  #increment j
            k += 1  #increment k