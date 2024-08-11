a = [6, 5, 3, 1, 8, 7, 2, 4]
print(a)


# go thru the list
def bubble_sort(m):
    for i in range(len(m)):
        # compare the pairs of elements that are not sorted yet and swap if necessary
        for j in range(len(m) - i - 1):
            if m[j] > m[j + 1]:
                t = m[j]
                m[j] = m[j + 1]
                m[j + 1] = t
    print(m)


bubble_sort(a)
