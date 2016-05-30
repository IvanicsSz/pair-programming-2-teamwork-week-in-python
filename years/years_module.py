import datetime


def years(age):
    now = datetime.datetime.now()
    return now.year + (100-age)


def main():
    name = input("What is your name? ")
    age = 0
    count = 0

    while not age or not count:
        try:
            age = int(input("How old are you? "))
            count = int(input("How many times do you want to print out the message?"))
        except ValueError as e:
            print("Please put number for your age and print out")
    when = years(age)

    while count:
            print("{0} you will be 100 years old in {1} ".format(name.title(), when))
            count -= 1
    return


if __name__ == '__main__':
    main()
