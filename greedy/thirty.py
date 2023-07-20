nums = list(map(int,list(input())))

if (sum(nums)%3 != 0) or ((0 in nums) == False):
    print(-1)
    exit(0)
else:
    nums.sort(reverse=True)
    print(''.join(str(i) for i in nums))