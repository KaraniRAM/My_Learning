int removeDuplicates(int* nums, int numsSize) {
    int n=numsSize,k=2;
    if (n==1) return n;
    for (int i=2;i<n;i++){
        if(nums[i]!=nums[k-2])
            nums[k++]=nums[i];    
    }
    return k;
}