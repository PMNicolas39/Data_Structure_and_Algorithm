def insert_sort(m):
    for i in range(len(m)):
        x = m[i]
        while i > 0 and m[i - 1] > x:
            m[i], m[i - 1] = m[i - 1], x
            i -= 1


def insert_sort2(m):
    for i in range(len(m)):
        x = m[i]
        j = i
        while j > 0 and m[j - 1] > m[j]:
            m[j], m[j - 1] = m[j - 1], m[j]
            j -= 1


a = [5, 6, 3, 1, 8, 7, 24]
a2 = [11, 3, 4, 5, 5, 63, 9]
insert_sort(a)
insert_sort2(a2)
print(a)
print(a2)
