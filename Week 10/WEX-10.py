#
# Weekly Exercise #10: Recursive Functions
# Author: Aditya Dube (G02500368)

#
# We have a triangle made of blocks. The topmost row has 1 block, the next
# row down has 2 blocks, the next row has 3 blocks, and so on. Compute
# recursively (no loops or multiplication) the total number of blocks in
# such a triangle with the given number of rows. The parameter rows indicates
# the number of rows in the triangle.
#
# Here are some sample calls:
#   triangle(0) returns 0
#   triangle(1) returns 1
#   triangle(2) returns 3
#   triangle(5) returns 15
#
def triangle(rows):
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows - 1)


#
# Given a nonnegative int n, return the sum of its digits recursively (no
# loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while floor divide (//) by 10 removes the rightmost digit (126 // 10 is 12).
#
# Here are some sample calls:
#   sum_digits(126) returns 9
#   sum_digits(49) returns 13
#   sum_digits(12) returns 3
#   sum_digits(5) returns 5
#   sum_digits(100) returns 1
#
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


#
# Given a string as input, compute recursively (no loops) the number of times
# lowercase "hi" appears in the string.
#
# Here are some sample calls:
#   count_hi("xxhixx") returns 1
#   count_hi("xhixhix") returns 2
#   count_hi("hi") returns 1
#   count_hi("hello") returns 0
#   count_hi("xyzhihiabchiparhihihi") returns 6
#
def count_hi(string):
    if len(string) < 2:
        return 0
    elif string[:2] == "hi":
        return 1 + count_hi(string[2:])
    else:
        return count_hi(string[1:])


#
# Let's test the above recursive functions - DO NOT MODIFY
#
def main():
    print(triangle(0))
    print(triangle(1))
    print(triangle(2))
    print(triangle(3))
    print(triangle(5))
    print(sum_digits(126))
    print(sum_digits(49))
    print(sum_digits(12))
    print(sum_digits(5))
    print(sum_digits(100))
    print(sum_digits(111))
    print(count_hi("xxhixx"))
    print(count_hi("xhixhix"))
    print(count_hi("hi"))
    print(count_hi("hello"))
    print(count_hi("xyzhihiabchiparhihihi"))


#
# Call main() if this script is run as a top-level program
#
if __name__ == "__main__":
    main()
