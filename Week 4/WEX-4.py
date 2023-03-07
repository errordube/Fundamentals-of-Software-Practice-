#
# Weekly Exercise #4: Strings, Lists, and Functions
# Author: Aditya Dube (G025003688)

import random

#
# A run is a sequence of adjacent repeated values.
#
# This function takes a positive integer (n) as input and performs the following STEPS:
#   1. Generates n random integers between 1 and 6 (representing a die toss)
#      and store these values in a list.
#   2. Applies the algorithm given in the execise to construct a string with
#      values in the list while marking the runs in the sequence by placing
#      them inside parentheses.
#   3. Returns the list of values and the generated string to the caller.
#
#   NOTE: Steps 1 and 3 are completed for you. Do not make changes to code
#         for these steps. Your task is to complete Step 2 in the function below.
#
def die_toss_seq_with_runs_marked(n):
    # STEP 1: generate a list of n random die numbers
    # (DO NOT CHANGE)
    values = []
    for i in range(n):
        values.append(random.randint(1,6))
    
    # STEP 2: COMPLETE THIS STEP
    # Apply the algorithm given in the exercise to construct a string with runs marked.
    # YOUR CODE FOR THIS STEP GOES AFTER THE STATEMENT BELOW
    result_str = ""
    in_run = False
    for i in range(n):
        if in_run and values[i] != values[i-1]:
            result_str += ") "
            in_run = False
        if not in_run and i < n-1 and values[i] == values[i+1]:
            result_str += f"( {values[i]} "
            in_run = True
        else:
            result_str += f"{values[i]} "
    if in_run:
        result_str += ") "



    # STEP 3: return the list of die tosses and string with runs marked as a tuple
    # (DO NOT CHANGE)
    return values, result_str.strip()


#
# main() function that calls die_toss_seq_with_runs_marked()
# DO NOT MAKE CHANGES TO THIS FUNCTION
#
def main():
    result = die_toss_seq_with_runs_marked(25)
    print("Die toss sequence:",result[0])
    print("Die toss sequence with runs marked:",result[1])


#
# call main() if this script is run as a top-level script (DO NOT CHANGE)
#
if __name__ == "__main__":
    main()
