
nums = list(map(int, input().split()))
sorted = []

def sort_dub(nums = []):
    for num in nums:
        if num not in sorted:
            sorted.append(num)
    return sorted

print(sort_dub(nums))
