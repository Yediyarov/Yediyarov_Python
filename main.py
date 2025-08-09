def hello_if_gt_seven(number: int):
    if number > 7:
        print("Hello")

def greet_name(user_name: str):
    if user_name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def multiples_of_three(numbers_list):
    return [num for num in numbers_list if num % 3 == 0]

def main():
    # 1) Number check
    try:
        entered_number = int(input("Enter a number: ").strip())
        hello_if_gt_seven(entered_number)
    except ValueError:
        print("Invalid number. Skipping number check.")

    # 2) Name check
    entered_name = input("Enter a name: ").strip()
    greet_name(entered_name)

    # 3) Multiples of 3
    array_input = input(
        "Enter numbers separated by commas (e.g., 1,3,6,8,9,12): "
    ).strip()

    if array_input:
        converted_numbers = []
        for element in array_input.split(","):
            try:
                converted_numbers.append(int(element.strip()))
            except ValueError:
                # Ignore invalid entries silently
                pass
        print("Multiples of 3:", multiples_of_three(converted_numbers))
    else:
        print("No array provided.")

if __name__ == "__main__":
    main()
