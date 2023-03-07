#
# Weekly Exercise #8: More on Classes in Python
# Author: Aditya Dube (G02500368)

class Letter(object):
    """Letter class for authoring a simple letter."""

    def __init__(self, letter_from, letter_to):
        """
        Initialize a Letter object's instance variables using the parameter values.

        Parameters:
            letter_from (str): name of the sender
            letter_to (str): name of the recipient

        Instance variables:
            _sender: initialized with the value of parameter letter_from
            _recipient: initialized with the value of parameter letter_to
            _body: a list (initially empty) to store the lines in the body of the letter
        """
        self._sender = letter_from
        self._recipient = letter_to
        self._body = []

    def letter_sender(self):
        """Return the value of self._sender instance variable."""
        return self._sender

    def letter_recipient(self):
        """Return the value of self._recipient instance variable."""
        return self._recipient
    
    def add_line(self, line):
        """Add a line of text to the body of the letter. A line could be an empty string (blank line)."""
        self._body.append(line)

    def letter_body(self):
        """
        Return a string value constructed using the lines from the body of the letter
        where each line in letter body is separated by a newline except the last line.
        """
        return "\n".join(self._body)

    def letter_text(self):
        """
        Return a string value that represents the entire text of the letter.
        Make use of letter_sender(), letter_recipient(), and letter_body() methods above
        to construct the result string.
        
        The constructed string has the following form:

            Dear recipient name:
            blank line
            first line of the letter body
            second line of the letter body
            ...
            last line of the letter body
            blank line
            Sincerely,
            blank line
            sender name

        Here is an example letter:

            Dear John:

            I am sorry we must part.
            I wish you all the best.

            Sincerely,

            Mary
        """
        letter = f"Dear {self._recipient}:\n\n{self.letter_body()}\n\nSincerely,\n\n{self._sender}"
        return letter

    def __eq__(self, other):
        """
        Return True if this (self) Letter object is value equal to the other object, False otherwise.
        Implement this method as we discussed in class (see code examples).

        Parameter:
            other: object to compare the self object to
        """
        if isinstance(other, Letter):
            return self._sender == other._sender and self._recipient == other._recipient and self._body == other._body
        return False

    def __str__(self):  # DO NOT MODIFY THIS METHOD
        """Return string representation of a Letter object."""
        return self.letter_text()
        

#
# DO NOT MODIFY THE CODE IN THIS FUNCTION
#
def main():
    # let's author a letter and print it
    letter = Letter("Mary","John")
    letter.add_line("I believe that the best friends would not say goodbye to each other.")
    letter.add_line("Therefore, accept this farewell message as a mere formality.")
    letter.add_line("")
    letter.add_line("Farewell my friend!")

    # print the letter
    print(letter)


# call main() if this script is run as a top-level program
if __name__ == "__main__":
    main()

