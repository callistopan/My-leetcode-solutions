int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

long long minOperationsToMakeMedianK(int* nums, int numsSize, int k) {
    long long res = 0;
    qsort(nums, numsSize, sizeof(int), compare);
    for (int i = 0; i <= numsSize/2; i++){
        res += fmax(0, nums[i] - k); // decrease excess numbers
    }
    for (int i = numsSize/2; i < numsSize; i++){
        res += fmax(0,k - nums[i]);
    }
    return res;    
}

//2,5,5,6,8 k= 7