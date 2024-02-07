
nums = list(map(int, input().split()))

def spy_game(nums = []):
    zeroes = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
        if zeroes == 2 and nums[i] == 7:
            return True
    return False

if spy_game(nums):
    print('True')
else:
    print('False')
