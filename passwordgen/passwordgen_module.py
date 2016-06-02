import random
import string


def passwordgen():
    weak_list = []
    pass_level = input("Please enter that you want weak or strong pass: ")
    pass_level = pass_level.lower()
    if (pass_level == "strong"):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        number = string.digits
        symbols = "!@#$%^&*()?"
        dictionary = [lower, upper, number, symbols]
        passw = [dictionary[i][random.randint(0, len(dictionary[i])-1)] for i in range(4)]
        passw2 = [dictionary[i][random.randint(0, len(dictionary[i])-1)] for i in range(4)]
        print("".join(passw) + "".join(passw2))
        return "".join(passw) + "".join(passw2)
    if (pass_level == "weak"):
        with open("/usr/share/dict/words", "r") as r:
            for index, line in enumerate(r):
                weak_list.append(line.replace("\n", ""))
        weak_list = (
            weak_list[random.randint(0, len(weak_list)-1)] +
            weak_list[random.randint(0, len(weak_list)-1)]
        )
        print(weak_list)
        return weak_list
def main():

    passwordgen()
    return


if __name__ == '__main__':
    main()
