#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

long long* construct_array(FILE* fp) {
    long long* nums = malloc(sizeof(long long) * SIZE);

    char buf[256];
    for (long long i = 0; i < SIZE; i++) {
        fgets(buf, sizeof(buf), fp);
        nums[i] = atoll(buf);
     }

    return nums;	
}

void max_two(long long* a, long long* b, long long* nums) {
	// set a and b to indices of two largest numbers in nums
	*a = 0;
	*b = 1;
	if (nums[0] < nums[1]) {
		*b = 0;
		*a = 1;
	}

	for (long long i = 2; i < SIZE; ++i) {
		if (nums[i] > nums[*a]) {
			*b = *a;
			*a = i;
		}
		else if (nums[i] > nums[*b]) {
			*b = i;
		}
	}
}

long long kk(long long* nums) {
	long long a = 0, b = 0;

	for (long long i = 0; i < SIZE; ++i) {
		max_two(&a, &b, nums);
		nums[a] = nums[a] - nums[b];
		nums[b] = 0;
	}

	max_two(&a, &b, nums);

	return nums[a];
}

int main(int argc, char* argv[]) {
    char* inputfile = argv[1];

    FILE* fp;
    fp = fopen(inputfile, "r");

    long long* nums = construct_array(fp);

    long long res = kk(nums);

    printf("%lld\n", res);

    return 0;
}
