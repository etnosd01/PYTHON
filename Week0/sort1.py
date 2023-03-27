def insertion_sort (ary):
    for i in range(1, len(ary)):
        for j in range(i, 0, -1):
            if ary[j] < ary[j - 1]:
                ary[j], ary[j - 1] = ary[j - 1], ary[j]
            else:
                break
    return ary

def selection_sort(ary):
    for i in range(len(ary)):
        min = 9999
        for j in range(i, len(ary)):
            if ary[j] < min:
                min = ary[j]
                index = j
        ary[i], ary[index] = ary[index], ary[i]
    return ary

def bubble_sort(ary):
    for i in range(len(ary), 0, -1):
        for j in range(1, i):
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
    return ary

def shell_sort(ary):
    k = len(ary) // 2
    while k > 0:
        for i in range(k, len(ary)):
            key = ary[i]
            h = i
            while h >= k and ary[h - k] > key:
                ary[h] = ary[h - k]
                h -= k
            ary[h] = key
        k = k // 2
    return ary