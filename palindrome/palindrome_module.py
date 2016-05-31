def palindrome(str):
    str_forward = str.replace(" ",'')
    str_backward = str[::-1].replace(" ",'')
    result = ""
    print(str_forward, str_backward)
    #print("".join(str_forward), "".join(str_backward))
    if str_forward.lower() == str_backward.lower():
        print(str_forward, str_backward)
        #if str_forward == str_backward:
        result = True
    else:
        result = False
    return result


def main():
    pali = input("Please write a string: ")
    if palindrome(pali):
        return print("Palindrome")
    else:
        return print("Not Palindrome")


if __name__ == '__main__':
    main()
