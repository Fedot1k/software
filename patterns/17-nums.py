with open('stuff/17-range.txt') as file:
    nums = [int(x) for x in file.readlines()]

res = []

maxElem = max([x for x in nums if x%10==7])


for i in range(len(nums) - 2):
    three = [nums[i], nums[i+1], nums[i+2]]

    first = [int(str(abs(x))[0]) for x in three]
    second = [x for x in three if len(str(abs(x))) == 3 and str(abs(x))[-1] == '7']

    if len(set(first)) == 1 and len(second) >= 1 and abs(sum(three)) < maxElem:
        res.append(abs(sum(three)))

print(len(res), max(res))