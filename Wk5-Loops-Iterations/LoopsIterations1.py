nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('Found', num, '\b!')
#         # break
#         continue
#     print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)
