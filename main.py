def find_target(arr, target):
    seen = {}
    for num in arr:
        if num in seen:
            return [num, seen[num]]
        seen[target - num] = num
    return []


print(find_target([3, 5, -4, 8, 11, 1, -1, 61], 10))