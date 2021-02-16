def ask_for_number():
    return input("Type nth number to be searched: ")


def check_number(num_str):
    try:
        return int(num_str) > 0
    except ValueError:
        return False


def show_error_message():
    print("Invalid input! Try again\n")


def generate_fibonacci_list(nth_number):
    fibonacci_list = [1, 1]
    for i in range(0, nth_number - 2):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list


def get_nth_number(fibonacci_list, nth_number):
    return fibonacci_list[nth_number - 1]


def show_nth_number(nth, nth_number):
    print(f"\n{nth}th position in Fibonacci Sequence is the number {nth_number}\n")


def main():
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
