l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[5,6,7],[8,9,10],[11,12,13]]

result = []
for x in range(len(l1)):
    ans = []
    for z in range(len(l1[x])):
        ans.append(l1[x][z] + l2[x][z])
    result.append(ans)

for val in result:
    for data in val:
        print(data,end=" ")
    print()