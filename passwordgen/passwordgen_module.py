import random


def passwordgen():
    box = [
        [97, 122],
        [65, 90],
        [48, 57],
        [35, 41],
    ]
    let = [chr(random.randint(box[i][0], box[i][1])) for i in range(4)]
    let2 = [chr(random.randint(box[i][0], box[i][1])) for i in range(4)]
    print("".join(let)+"".join(let2))
    return "".join(let)+"".join(let2)


def main():

    passwordgen()
    return


if __name__ == '__main__':
    main()
