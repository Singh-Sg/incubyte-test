import re  # Regular expression 


class Calculator:
    def calculate_sum(self, numbers):
        if not numbers:  # input string is empty return 0
            return 0

        negative_numbers = []
        # string starts with "//"
        if numbers.startswith("//"):
            delimiter = numbers[2:3]  # extract custom delimiter
            numbers = numbers[4:]  # remove the delimiter

            # split the numbers by the custom delimiter or newline
            numbers_list = re.split(f"[{delimiter}\n]", numbers)

            # check negative
            for num in numbers_list:
                num = int(num)

                if num < 0:
                    negative_numbers.append(num)  # add negative_numbers list

            if negative_numbers:
                raise ValueError(
                    f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
                )

            # Return sum integers
            return sum(map(int, numbers_list))

        else:
            # split the numbers
            numbers_list = re.split("[,\n]", numbers)

            for num in numbers_list:
                num = int(num)
                if num < 0:
                    negative_numbers.append(num)

            if negative_numbers:
                raise ValueError(
                    f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}"
                )

            return sum(map(int, numbers_list))


if __name__ == "__main__":
    calculator = Calculator()

    try:
        print(calculator.calculate_sum(""))  # return 0
        print(calculator.calculate_sum("1"))  # return 1
        print(calculator.calculate_sum("1,5"))  # return 6
        print(calculator.calculate_sum("1\n2,3"))  # return 6
        print(calculator.calculate_sum("//;\n1;2"))  # return 3
        print(
            calculator.calculate_sum("1,2,-3,4")
)  # raise an exception due to negative number (-3)

    # Handle Exception
    except ValueError as ex:
        print(ex)  # This will print the error message
