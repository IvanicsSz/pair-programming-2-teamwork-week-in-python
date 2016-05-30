import random
def listoverlap(list1, list2):
    return list(set(list1) & set(list2))


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = listoverlap(a, b)
    d, e = [random.randint(0, 20) for i in range(random.randint(1,20))], [random.randint(0, 20) for j in range(random.randint(1,20))]
    f = listoverlap(d, e)
    # print (d, e, f)
    return


if __name__ == '__main__':
    main()
