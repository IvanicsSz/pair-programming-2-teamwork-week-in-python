def palindrome(str):
    str_forward = str.replace(" ", '')
    str_backward = str[::-1].replace(" ", '')
    if str_forward.lower() == str_backward.lower():
        return True
    return False


def main():
    pali = input("Please write a string: ")
    if palindrome(pali):
        return print("Palindrome")
    else:
        return print("Not Palindrome")


if __name__ == '__main__':
    main()
