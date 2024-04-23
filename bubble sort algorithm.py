def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


n = int(input())
nums = list(map(int, input().split()))

bubble_sort(nums)

print(*nums)
