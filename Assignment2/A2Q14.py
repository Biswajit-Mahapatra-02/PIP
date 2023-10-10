def UpperCase(char):
    assert 'a' <= char <= 'z', "Invalid input. Enter lower case only."
    assert len(char) == 1, "Invalid input. Enter a single character only."
    return chr(ord(char)-32)
def main():
    while True:
        user_input = input("Enter lower case alphabet, quit to exit: ")
        if user_input == 'quit':
            print("Exiting...")
            break
        try:
            upper = UpperCase(user_input)
            print(f"The upper case of {user_input} is {upper}")
        except AssertionError as e:
            print(e)
main()
