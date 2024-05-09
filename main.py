def calculate_check_digit(isbn):
    total = 0
    for i in range(10, 1, -1):
        # The number has 10 information digits and ends with 1 check digit.
        # Assuming the digits are "abcdefghij-k" where k is the check digit. Then the check digit is computed by the following formula:
        # k = ( [a b c d e f g h i j] * [1 2 3 4 5 6 7 8 9 10] ) modulus 11. If the result is 10, the check digit is X.
        # Instead of making a big numbers list, we can just iterate from 9 to 1 and multiply the number by the position, way more efficient.
        total += int(isbn[10 - i]) * i
    check_digit = 11 - (total % 11)
    if check_digit == 10:
        return 'X'
    else:
        return str(check_digit)

book_num = input("Enter the 10 digit number: ")
# check if the input is a 10 digit number
if len(book_num) == 10 and book_num.isdigit():
    isbn = book_num + calculate_check_digit(book_num)
    print("The ISBN number for this book is:", isbn)
else:
    print("Invalid input. Please enter a 10 digit number.")