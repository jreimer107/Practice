arr = [1, 5, 4, 0, 9, 0, 8]

# Pull out zeros into their own array
# O(N)
zeros = []
nonzeros = []
for num in arr:
    if num == 0:
        zeros.append(num)
    else:
        nonzeros.append(num)

# Put the others on the end
# O(N)
zeros.extend(nonzeros)

print(zeros)
