class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people_sorted=sorted(people,key= lambda x:x[0])
            
        least_front_most=sorted(people,key= lambda x:x[1])
       
            
        seen=set()
        look_up={}
        for i in range(len(people)):
            h,k=least_front_most[i]
            look_up[(h,k)]=i
            
            
        for people in people_sorted:
            h,k=people
            index=look_up[(h,k)]
            count=0

            for i in range(len(least_front_most)):
                if count==k and (least_front_most[i][0],least_front_most[i][1]) not in seen:
                    least_front_most[index],least_front_most[i]=least_front_most[i],least_front_most[index]           
                    look_up[(least_front_most[index][0],least_front_most[index][1])]=index
                    seen.add((h,k))
                    break
                    
                if count<k and least_front_most[i][0]>=h:
                    count+=1
        return least_front_most