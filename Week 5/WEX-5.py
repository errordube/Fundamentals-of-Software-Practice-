#
# Weekly Exercise #5: More on Lists
# Author: Aditya Dube (G02500368)

import random

def main():
    print("This program prints ten random permutations of the numbers 1 to 10.\n")

    # each iteration of this loop generates one random permutation of numbers 1 t0 10
    for i in range(10):

        list_one = [x for x in range(1, 11)]
        # TO DO:
        # Fill the list "list_one" with numbers 1 to 10
        # PLACE YOUR CODE BELOW



        # permuted_list initialzed to an empty list (DO NOT CHANGE)
        permuted_list = []

        #
        # TO DO:
        # Let's generate one permutation of numbers 1 to 10 using the following algorithm:
        # Write a for loop that runs 10 times and perform the following actions in its body
        #     - pick a random position in list_one
        #     - store this position in variable called pos
        #     - remove the number at the pos from list_one (using list_one.pop(pos) operation)
        #     - append the number removed to permuted_list
        # PLACE YOUR CODE BELOW
        for j in range(10):
            pos = random.randint(0, len(list_one) - 1)
            number = list_one.pop(pos)
            permuted_list.append(number)




        # print the permuted_list to console (DO NOT CHANGE)
        print(permuted_list)


# call main() if this script is run as a main program
if __name__ == "__main__":
    main()
