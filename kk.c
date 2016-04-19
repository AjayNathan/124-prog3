#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

int* construct_array(FILE* fp) {
    int* nums = malloc(sizeof(int) * SIZE);

    char buf[256];
    for (int i = 0; i < SIZE; i++) {
        fgets(buf, sizeof(buf), fp);
        nums[i] = atoi(buf);
     }

    return nums;	
}

void max_two(int* a, int* b, int* nums) {
	// set a and b to indices of two largest numbers in nums
	*a = 0;
	*b = 1;
	if (nums[0] < nums[1]) {
		*b = 0;
		*a = 1;
	}

	for (int i = 2; i < SIZE; ++i) {
		if (nums[i] > nums[*a]) {
			*b = *a;
			*a = i;
		}
		else if (nums[i] > nums[*b]) {
			*b = i;
		}
	}
}

int kk(int* nums) {
	int a = 0, b = 0;

	for (int i = 0; i < SIZE; ++i) {
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

    int* nums = construct_array(fp);

    int res = kk(nums);

    printf("%d\n", res);

    return 0;
}
