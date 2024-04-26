int findSpecialInteger(int* arr, int arrSize) {
    int count = 1;
    int ans = -1;
    for (int i = 1; i< arrSize; i++){
        if ( arr[i-1] == arr[i]){
            count++;
            if(count > arrSize/4){
                ans = arr[i];
                return ans;
            }
        }
        else{
            count = 1;
        }
    }
    return arr[0];
}