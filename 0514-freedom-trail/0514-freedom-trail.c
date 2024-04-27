int findRotateSteps(char* ring, char* key) {
    int ringLength = strlen(ring);
    int keyLength = strlen(key);
    int** bestSteps =(int**)malloc(sizeof(int*)*101);
    for(int i = 0; i < 101; i++){
        bestSteps[i] = (int*)malloc(sizeof(int)*101);
    }
    for(int i = 0; i < 101; i++){
        for(int j = 0; j < 101; j++){
            bestSteps[i][j] = -1;
        }
    }
    int ans = try_lock(0,0,ring,key,bestSteps);
    for(int i = 0; i < 100;i++){
        free(bestSteps[i]);
    }
    free(bestSteps);
    return ans;
}

int try_lock(int ring_index,int key_index,char* ring,char* key, int** bestSteps){
    if(bestSteps[ring_index][key_index] != -1){
        return bestSteps[ring_index][key_index];
    }
    if( key_index == strlen(key)){
        bestSteps[ring_index][key_index] = 0;
        return 0;
    }
    int min_steps = INT_MAX;
    for (int i = 0; i < strlen(ring); i++){
        if(ring[i] == key[key_index]){
            min_steps = fmin(min_steps, count_steps(ring_index,i,strlen(ring))+1+ try_lock(i,key_index+1,ring,key,bestSteps));
        }
    }
    bestSteps[ring_index][key_index] = min_steps;
    return min_steps;
}

int count_steps(int curr, int next, int ringLength){
    int stepsBetween = abs(curr - next);
    int stepsAround = ringLength - stepsBetween;
    return fmin(stepsBetween , stepsAround);
}