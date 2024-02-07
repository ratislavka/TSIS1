nums = []
nums.append(int (input()))
prime_nums = []

def filter_prime(nums):
    for num in nums:
        if num == 1 or nums == 2:
            prime_nums.append(num)
        elif num > 2 and num:
            prime_nums.append(num)

filter_prime(nums)

print(f'Prume numbers: {prime_nums}')
