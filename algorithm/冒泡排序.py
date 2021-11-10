a = [9, 3, 7, 2, 1, 6, 8]


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


if __name__ == '__main__':
    bubble_sort(a)
    print(a)

