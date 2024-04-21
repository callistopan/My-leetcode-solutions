int sumOfTheDigitsOfHarshadNumber(int x) {
    int digit_sum = 0;
    int temp = x;
    while (temp !=0){
        digit_sum += temp % 10;
        temp /=10;
    }
    
    if ( x % digit_sum == 0){
        return digit_sum;
    }
    return -1;
}