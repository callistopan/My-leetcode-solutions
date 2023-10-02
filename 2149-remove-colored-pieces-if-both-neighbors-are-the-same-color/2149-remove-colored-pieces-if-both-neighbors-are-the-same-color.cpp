class Solution {
public:
    bool winnerOfGame(string colors) {
        // all moves are already available to both players
        // number of moves available to both players at the start of the game
        int alice = 0;
        int bob = 0;

        for (int i = 1 ;i < colors.size() -1 ; i++ ){
            if (colors[i-1] == colors[i] && colors[i] == colors[i+1]){
                if (colors[i] == 'A'){
                    alice++;
                }
                else{
                    bob++;
                }
            }
        }
        return alice - bob >= 1;
        
    }
};