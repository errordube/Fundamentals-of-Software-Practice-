#
# Weekly Exercise #6: Files and Exceptions
# Author: Aditya Dube (G02500368)

import sys

#
# This program requires names of input and output files as command line arguments and
# the program performs the following actions.
# 
# It determines the following information about the contents of the input file:
#   1. Number of lines in the input file
#   2. Number of words in the input file. A word is defined as a sequence of
#      characters separated by whitespace
#   3. Number of words in the input file that end with a punctuation mark
#      Characters that are considered punctuation marks: . , : ; ? !
#   4. Number of words in the input file that do not end with a punctuatin mark
#   5. Number of characters in the input file including spaces and newline characters
#
# The program then writes the above information to the specified output file in the following format:
#
#   Information about input file <infilename>:
#
#   Number of lines: 
#   Number of words:
#   Number of words that end with a punctuation mark:
#   Number of words that end without a punctuation mark:
#   Number of characters:
#
# You are given two sample input files to test your program: input1.txt and input2.txt (DO NOT CHANGE)
# 
# You can test this program by using the following command from the command prompt:
#
#   python WEX-6.py input1.txt output1.txt     (To process input1.txt file)
#
#   python WEX-6.py input2.txt output2.txt     (To process input2.txt file)
#
# TO DO ==> THE ONLY THING FOR YOU TO DO IS TO COMPLETE THE BODY OF "for loop" AT LINE 67
#   
def main():
    # check if the program is invoked correctly (i.e., invokved with three command line arguments)
    if len(sys.argv) != 3:
        print("Incorrect program invocation - missing command line argument(s)...")
        print("Coorect usage: python WCE-4.py infilename outfilename")
        sys.exit()

    # retrieve the input file name from command line arguments
    infilename = sys.argv[1]

    # retrieve the output file name from command line arguments
    outfilename = sys.argv[2]

    try:
        infile = open(infilename, "r")
        outfile = open(outfilename, "w")

        try:
            # initialize appropriate counters
            nbr_lines = 0
            nbr_words = 0
            nbr_words_with_punct_marks = 0
            nbr_chars = 0

            # process each line in the input file to update counters nbr_lines, nbr_chars,
            # nbr_words, and nbr_words_with_punct_marks
            for line in infile:
                # TO DO: REPLACE THE "pass" STATEMENT BELOW WITH YOUR CODE
                nbr_lines += 1
                nbr_chars += len(line)

                # split the line into words
                words = line.split()

                # count the number of words and the number of words that end with a punctuation mark
                for word in words:
                    nbr_words += 1

                    # count the number of words that end with a punctuation mark
                    if word[-1] in ['.', ',', ':', ';', '?', '!']:
                        nbr_words_with_punct_marks += 1


            # DO NOT CHANGE FROM THIS POINT ON
            nbr_words_without_punct_marks = nbr_words - nbr_words_with_punct_marks

            # write input file information to the output file
            outfile.write(f"Information about input file {infilename}\n\n")
            outfile.write(f"Number of lines: {nbr_lines}\n")
            outfile.write(f"Number of words: {nbr_words}\n")
            outfile.write(f"Number of words that end with a punctuation mark: {nbr_words_with_punct_marks}\n")
            outfile.write(f"Number of words that end without a punctuation mark: {nbr_words_without_punct_marks}\n")
            outfile.write(f"Number of characters: {nbr_chars}\n")
        finally:
            infile.close()
            outfile.close()

    except OSError as ex:
        print(ex)


# call main() if this script is run as a main program
if __name__ == "__main__":
    main()
