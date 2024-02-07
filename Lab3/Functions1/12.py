
nums = list(map(int, input().split()))

def histogram(nums):
    for num in nums:
        print('*' * num) #The * operator repeats the string that number of times.

histogram(nums)