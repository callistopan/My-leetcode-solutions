class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        
        int distance = 0;
        
        while (mainTank >=5 && additionalTank){
            distance += 50;
            additionalTank--;
            mainTank -= 5;
            mainTank++;
            
        }
        distance += (mainTank * 10); // remaining fuel
        return distance;
    }
};