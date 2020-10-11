arr = [10, 2, 3, 18, 100, 500, 20, 1, 5, 19, 6]
target = 7

# First sort, O(logN)
arr.sort()
# print(arr)

# Numbers in array may be larger than the target sum.
# Numbers are even larger due to minimum being smallest number
# Need to find the index where the number plus the smallest number is smaller than the target
# And the next number plus the smallest number is larger.
# This is the cutoff point.
# Do binary search to find this. O(logN).
# If negative numbers are allowed, do another for the other way?
p1 = 0
p2 = len(arr) // 2
curr = arr[p2]
nxt = arr[p2 + 1]
tempTarget = target - arr[0]
while not (curr <= tempTarget and nxt > tempTarget):
    # print("Looking for top of array at index %d: %d" % (p2, arr[p2]))
    p2 += p2 // 2 if curr < tempTarget else -(p2 // 2)
    curr = arr[p2]

    # Stop if we're at the end
    if p2 == len(arr) - 1:
        break
    nxt = arr[p2 + 1]
    
# Now tune the numbers.
# If sum is too large, move larger number down.
# If sum is too small, move smaller number up
# Continue until found or until the two meet/cross.
# Linear search O(N)
# print("Looking between %d: %d and %d: %d" % (p1, arr[p1], p2, arr[p2]))
while curr != target and p1 < p2:
    curr = arr[p1] + arr[p2]
    # print("curr: " + str(curr))
    if curr > target:
        p2 -= 1
    elif curr < target:
        p1 += 1

if curr == target:
    print("Found target with %d and %d" % (arr[p1], arr[p2]))
else:
    print("Did not find target")


# After all this, it is O(N), but the binary search makes the typical case a lot better.