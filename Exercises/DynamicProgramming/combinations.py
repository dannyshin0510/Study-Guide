# BANK
list = [1,2,3,4]


print('All subsets')
def recur(currIndex, subset):
    print(subset)
    for i in range(currIndex, len(list)):
        subset.append(list[i])
        recur(i+1, subset)
        subset.pop(-1)
recur(0, [])


print('All subsets of length n=3')
def recur(currIndex, subset):
    if len(subset) == 3:
        print(subset)
    for i in range(currIndex, len(list)):
        subset.append(list[i])
        recur(i+1, subset)
        subset.pop(-1)
recur(0, [])

print('All possible combination of length n=3')
def recur(subset):
    if len(subset) == 3:
        print(subset)
        return
    for i in range(0, len(list)):
        subset.append(list[i])
        recur(subset)
        subset.pop(-1)
recur([])

print('All combinations, but each element only once')
listings = []
def recur(combo, nums):
    if combo != []:
        listings.append(combo)
    if len(nums) == 0:
        return
    for i in range(len(nums)):
        print (nums[:i], nums[i+1:])
        recur(combo+[nums[i]], nums[:i]+nums[i+1:])
recur([], list)
print (listings)


print('sliding window')
total = 5
l=0
for r in range(0, len(list)):
    if sum(list[l:r]) > 5:
        l+=1
    if sum(list[l:r]) == 5:
        print(list[l:r])