def sliding_window(nums, k):
    if not nums:
        return []
    n = len(nums)
    if n * k == 0:
        return []
    output = []
    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n-1]
    for i in range(1, n):
        if i % k == 0:
            left[i] = nums [i]
        else:
            left[i] = max(left[i - 1], nums[i])
    for i in range(n -2, -1, -1):
        if (i + 1) % k == 0:
            right[i] = nums[i]
        else:
            right[i] = max(right[i + 1], nums[i])
    for i in range(n - k +1):
        output.append(max(right[i], left[i + k -1]))
    return output
nums = [9, 7, 2, 4, 6, 8, 2, 1, 5]
k = 4
sliding_window(nums, k)
result = sliding_window(nums,k)
print("Input:", nums)
print("window size:", k)
print("output:", result)