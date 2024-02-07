
nums = list(map(int, input().split()))

def has33(nums = []):
    for i in range(len(nums)- 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

if has33(nums):
    print('True')
else:
    print('False')
