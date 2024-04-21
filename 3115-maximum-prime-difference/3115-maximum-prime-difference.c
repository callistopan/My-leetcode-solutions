bool* sieveOfEratosthenes(int n){
    bool* primes = malloc(sizeof(bool)*(n+1));
    for (int i = 0 ; i<=n; i++){
        primes[i] = true;
    }
    primes[0] = false;
    primes[1] = false;
    for (int i = 2; i*i <= n; i++){
        if (primes[i]){
            for(int j = i*i; j <= n; j+=i){
                primes[j] = false;
            }
        }
    }
    return primes;
}
int maximumPrimeDifference(int* nums, int numsSize) {
    bool* primes = sieveOfEratosthenes(101);
    int ans = 0;
    int firstPrime = -1;
    int j = 0;
    while (j < numsSize){
        if(primes[nums[j]]){
            if(firstPrime != -1){
                ans = j - firstPrime;
            }
            else{
                firstPrime = j;
            }
        }
        j++;
    }
    return ans;
}

