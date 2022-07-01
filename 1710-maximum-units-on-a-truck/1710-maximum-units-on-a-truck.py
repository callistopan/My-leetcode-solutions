class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key= lambda x:-x[1])
        print(boxTypes)
        
        total=0
        
        for boxes,unit in boxTypes:
            
            if boxes <= truckSize:
                total+=boxes*unit
                truckSize-=boxes
                
            else:
                total+= truckSize*unit
                return total
        return total
                