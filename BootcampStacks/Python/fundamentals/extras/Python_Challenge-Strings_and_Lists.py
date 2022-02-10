"""
First, you will write a function called singleline_diff that takes two single line strings. You may assume that both strings are always a single line and do not contain any newline characters. The function should return the index of the first character that differs between the two lines.  If the lines are the same, the function should return the constant \color{red}{\verb!IDENTICAL!}IDENTICAL, which is already defined to be -1−1 in the provided template file.

If the lines are different lengths, but the entire shorter line matches the beginning of the longer line, then the first difference is located at the index that is one past the last character in the shorter line.  In other words, no character after the end of the shorter line is defined to be different than whatever character exists in the longer line at that location.

"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    return ""

    """
    Next, you will write a function called singleline_diff_format that takes two single line strings and the index of the first difference and will generate a formatted string that will allow a user to clearly see where the first difference between two lines is located. A user is likely going to want to see where the difference is in the context of the lines, not just see a number. Your function will return a three line string that looks as follows:

{\verb!abcd!}\\{\verb!==^!}\\{\verb!abef!}abcd
==^
abef

The format of these three lines is:

The complete first line.

A separator line that consists of repeated equal signs ("=") up until the first difference. A "^" symbol indicates the position of the first difference.

The complete second line.

If either line contains a newline or carriage return character ("\n" or "\r") then the function returns an empty string (since the lines are not single lines and the output format will not make sense to a person reading it).

If the index is not a valid index that could indicate the position of the first difference of the two input lines, the function should also return an empty string (again because the output would not make sense otherwise).  It must therefore be between 0 and the length of the shorter line. Note that you do not need to check whether the index actually identifies the correct location of the first difference, as that should have been computed correctly prior to calling this function.

    """

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    return (IDENTICAL, IDENTICAL)
    """
    Next, you will write a function called multiline_diff that takes two lists of single line strings. You may assume that the strings within the lists are all single lines. The function returns a tuple that indicates the line and index within that line where the first difference between the two lists occurs.  If the contents of the two lists are the same, the function should return the tuple \color{red}{\verb!(IDENTICAL, IDENTICAL)!}(IDENTICAL, IDENTICAL).  (Recall that the constant \color{red}{\verb!IDENTICAL!}IDENTICAL is already defined to be -1−1 in the provided template file.)

The definition of whether two lines are the same or different and the resulting index for location of a difference is the same as it was for \color{red}{\verb!singleline_diff!}singleline_diff.

The line on which the first difference occurs should be the index into the input lists that correspond to that line. If the input lists are different lengths, but the entire shorter list matches the beginning of the longer list, the first difference is located at the line that is one past the last line in the shorter list at index 0.  In other words, no character on the line after the end of the shorter list is defined to be different than whatever character exists on that line in the longer list.
    """
    """
    Next, you will write a function called get_file_lines that takes a filename as input. You may assume that the input names a file that exists and is readable. The function returns a list of single line strings, where each element of the list is one line from the file. The strings within the returned list should not contain any newline or carriage return ("\n" or "\r") characters.

    """
def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return []


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""
