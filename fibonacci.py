"""
User type a positive integer number
The script shows the nth-position of that number on the Fibonacci Sequence

e.g. Input '3' returns '2', because the third number in the Fibonacci Sequence is '2'
"""


def ask_for_number():
    """ Return the user input """
    return input("Type nth number to be searched: ")


def check_number(num_str):
    """
    Return True if user input is valid. Otherwise, returns False
    User's input is invalid when is not a integer or is negative
    """
    try:
        return int(num_str) > 0
    except ValueError:
        return False


def show_error_message():
    """ Prints an error message """
    print("Invalid input! Try again\n")


def generate_fibonacci_list(nth_number):
    """ Generates fibonacci list until the nth-number"""
    fibonacci_list = [1, 1]
    for _ in range(0, nth_number - 2):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list


def get_nth_number(fibonacci_list, nth_number):
    """ Get the nth-number from the Fibonacci Sequence """
    return fibonacci_list[nth_number - 1]


def show_nth_number(nth, nth_number):
    """ Show the Fibonacci Number """
    print(f"\n{nth}th position in Fibonacci Sequence is the number {nth_number}\n")


def main():
    """ Main function: execute the other functions"""
    nth_str = ask_for_number()
    if not check_number(nth_str):
        show_error_message()
        main()

    nth = int(nth_str)
    fibonacci_list = generate_fibonacci_list(nth)

    nth_number = get_nth_number(fibonacci_list, nth)
    show_nth_number(nth, nth_number)


# Main
main()
