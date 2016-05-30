def fizzbuzz(number):
    return 'Fizz'*(not number % 3)+''*(not number % 15)+'Buzz'*(not number % 5) or number


def main():
    num = ""
    for i in range(1, 101):
        num = fizzbuzz(i)
        print(num)
    return

if __name__ == '__main__':
    main()
