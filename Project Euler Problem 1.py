x=0
nums = []
while x < 999:
    x = x + 1
    if x%5 == 0:
        nums.append(x)
    elif x%3 == 0:
        nums.append(x)
    else:
      continue
print(nums)

b = sum(nums)
print(b)

