def quick_merge(list1, list2):
    result = []
    p1, p2 = 0, 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

def str_to_int(e):
    for i in range(len(e)):
        e[i] = int(e[i])
    return e

n = int(input())
list1 = str_to_int(input().split())
for i in range(n-1):
    list2 = str_to_int(input().split())
    list1 = quick_merge(list1, list2)

print(*list1)