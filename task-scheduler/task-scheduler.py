class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=[0]*26
        max_=0    # max frquency element frquency
        maxCount=0  # count of most frequencies
        for task in tasks:
            c=ord(task)-ord('A')
            counter[c]+=1
            
            if max_==counter[c]:
                maxCount+=1
            
            elif max_ < counter[c]:
                max_=counter[c]
                maxCount=1
        
        partCount=max_-1  # number of parts after first arrangement
        partLength=n-(maxCount-1)   # length of each part
        
        emptySlots=partCount*partLength #number of empty slots
        
        availableTasks=len(tasks)-max_ * maxCount #availble tasks
        
        idles = max ( 0, emptySlots- availableTasks)
        
        return len(tasks)+ idles
    
    '''you can always put more tasks in each part once you met the "minimum" requirement.'''
        