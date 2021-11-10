a = [9, 6, 1, 3, 5]


def insert_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
    return l


if __name__ == '__main__':
    insert_sort(a)
    print(a)
