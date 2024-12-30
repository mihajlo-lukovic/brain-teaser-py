"""
Break palindrome so that only one character is replaced in the given string
If given string is not a palindrome print IMPOSSIBLE
If string len is 1 or less than 1 print IMPOSSIBLE
If string contain same characters change character of last character in string
"""

BREAK_PALINDROME_FAILED = 'IMPOSSIBLE'


def check_palindrome(palindrome_str) -> bool:
    input_index = int(len(palindrome_str) / 2)

    reverse_check = -1
    for index, forward in enumerate(palindrome_str):
        if forward != palindrome_str[reverse_check]:
            return False

        if input_index == index:
            return True

        reverse_check -= 1


def determine_letter_to_use(palindrome_str) -> str:
    if palindrome_str[0] != 'a':
        return 'a'
    else:
        letter_count_first = 0
        letter_count_second = 0

        for letter in palindrome_str:
            if letter == 'a':
                letter_count_first += 1
            else:
                letter_count_second += 1

        if len(palindrome_str) - letter_count_first - 1 == 0:
            return 'b'
        else:
            return 'a'


def main():
    palindrome_str = str(input(
        'Enter palindrome that should be break from being a palindrome: '
    ))

    # Get string in lower case
    palindrome_str = palindrome_str.lower()

    # Get string without spaces
    palindrome_str = palindrome_str.replace(' ', '')

    # If given string is not a palindrome print IMPOSSIBLE
    if not check_palindrome(palindrome_str=palindrome_str):
        print(BREAK_PALINDROME_FAILED)
        return

    # If string len is 1 or less than 1 print IMPOSSIBLE
    if len(palindrome_str) <= 1:
        print(BREAK_PALINDROME_FAILED)
        return

    # Determine letter to use
    letter = determine_letter_to_use(palindrome_str=palindrome_str)

    for index in range(len(palindrome_str)):
        # Break palindrome so that only one character is replaced in the
        # given string
        if palindrome_str[index] != letter:
            print(
                f'{palindrome_str[:index]}{letter}{palindrome_str[index + 1:]}'
            )
            break
    else:
        # If string contain same characters change character of
        # last character in string
        print(f'{palindrome_str[:-1]}b')
