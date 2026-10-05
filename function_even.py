def isEven(integer):
    return integer % 2 == 0


def isPrimeNumber(integer):
    if integer <= 1:
        return False

    for i in range(2, integer):
        if integer % i == 0:
            return False

    return True


def subtract(first_integer, second_integer):
    return abs(first_integer - second_integer)


def divide(first_integer, second_integer):
    if second_integer == 0:
        return 0

    return first_integer / second_integer


def factorOf(integer):
    count = 0

    for i in range(1, integer + 1):
        if integer % i == 0:
            count += 1

    return count


def isSquare(integer):
    if integer < 0:
        return False

    for i in range(1, integer + 1):
        if i * i == integer:
            return True

    return False


def isPalindrome(integer):
    number = str(integer)
    return number == number[::-1]


def factorialOf(integer):
    factorial = 1

    for i in range(1, integer + 1):
        factorial = factorial * i

    return factorial


def squareOf(integer):
    return integer * integer


result = isEven(10)
result_two = isPrimeNumber(7)
result_three = subtract(3, 7)
result_four = divide(10, 2)
result_five = divide(10, 0)
result_six = factorOf(10)
result_seven = isSquare(25)
result_eight = isPalindrome(54145)
result_nine = factorialOf(5)
result_ten = squareOf(5)


print(result)
print(result_two)
print(result_three)
print(result_four)
print(result_five)
print(result_six)
print(result_seven)
print(result_eight)
print(result_nine)
print(result_ten)
