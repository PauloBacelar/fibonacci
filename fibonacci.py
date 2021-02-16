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


def main():
    nth_number_str = ask_for_number()
    if not check_number(nth_number_str):
        show_error_message()
        main()

    nth_number = int(nth_number_str)
    generate_fibonacci_list(nth_number)


# Main
main()
