/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numOfBurgers(int tomatoSlices, int cheeseSlices, int* returnSize) {
    
    int* ans = (int*)malloc(2*sizeof(int));
    if(tomatoSlices % 2 == 1 || (tomatoSlices/2) - cheeseSlices < 0 || 2*cheeseSlices - (tomatoSlices/2) < 0){
        int* empty = (int*)malloc(0*sizeof(int));
        *returnSize = 0;
        return empty;
    }
    ans[0] = (tomatoSlices/2) - cheeseSlices;
    ans[1] = 2*cheeseSlices - (tomatoSlices/2);
    *returnSize = 2;
    return ans;
}


/*[x,y]

x*4 + y*2 = tomatoSlices

x + y = cheeseSlices

y = cheeseSlices - x

x*4 + (cheeseSlices -x)2 = tomatoSlices

2*cheeseSlices + 2*x = tomatoSlices
x = tomatoSlices/2 - cheeseSlices
*/