"""
Fibonacci series is the sequence where each number is the sum of the previous two numbers of the sequence
Fibonacci sequence will be stopped after n execution which is provided in the user input
Results will be printed in console
"""


def main():
    execution_number = int(input('Enter the fibonacci sequence execution number: '))

    count = 1
    first_number = 0
    second_number = 1

    result: list = []

    while count <= execution_number:
        # Calculate iteration result
        sequence_result = first_number + second_number

        # Add iteration result into result list
        result.append(sequence_result)

        # Allocate second_number value to first_number before next iteration
        first_number = second_number

        # Allocate sequence_result value to second_number before next iteration
        second_number = sequence_result

        # Increase counter
        count += 1

    # Print fibonacci results
    print(result)
