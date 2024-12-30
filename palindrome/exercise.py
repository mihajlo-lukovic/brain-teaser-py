"""
Check if the given input is a palindrome

Simple true/false will be returned in the console
"""


def should_break(input_index: int, current_index: int) -> bool:
    if input_index == current_index:
        return True


def main():
    input_check_palindrome = input('Enter text to check palindrome: ')

    # Get string with all lower case characters
    input_check_lower = input_check_palindrome.lower()

    # Remove input_check spaces
    input_check = input_check_lower.replace(' ', '')

    # Get the middle index of the input_check
    input_index = int(len(input_check) / 2)

    reverse = -1
    for index, forward in enumerate(input_check):
        if forward != input_check[reverse]:
            # Characters are not the same, break loop and print negative result
            print(f'{input_check_palindrome} is palindrome: {False}')
            break

        if should_break(input_index=input_index, current_index=index):
            # Loop is in the input_check middle break loop
            # and print positive result
            print(f'{input_check_palindrome} is palindrome: {True}')
            break

        # Decrease variable that is used for input_check access by index
        # from reverse
        reverse -= 1
