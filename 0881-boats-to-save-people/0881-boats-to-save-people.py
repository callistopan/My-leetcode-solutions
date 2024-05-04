class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        sort the people in increasing order
        one pointer from beginning and one from end
        if both can go increse the light pointer also
        else decrese the heavy one only impliying that only the heavy man 
        can travel in that boat
        '''
        boats=0
        people.sort()
        light,heavy=0,len(people)-1
        while light<=heavy:
            boats+=1
            if people[light]+people[heavy]<=limit:
                light+=1
            heavy-=1
            
        return boats