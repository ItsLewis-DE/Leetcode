bool increasingTriplet(int* nums, int numsSize) {
    long long first = LLONG_MAX,second = LLONG_MAX;
    for(int i=0;i<numsSize;i++) {
        if (nums[i] <= first) {
            first = nums[i];
        }
        else if ( nums[i] <= second) {
            second = nums[i];
        }
        else {
            return true;
        }
    }
    return false;
}