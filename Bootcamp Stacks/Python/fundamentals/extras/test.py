"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
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
    line1_split = line1.split();
    line2_split = line2.split();
    for x, y in zip(line1_split,line2_split):
        if x != y:
            diff_index = line1_split.index(x)
            return diff_index
        # comment: 
    # END FOR

line1 = "She wasn't doing a thing that I could see, except standing there leaning on the balcony railing, holding the universe together"
line2 = "She wasn't doing a thing that I could see, except standing there sitting on the stairs, holding the universe together"

print(singleline_diff(line1,line2))

# def singleline_diff_format(line1, line2, idx):
#     """
#     Inputs:
#       line1 - first single line string
#       line2 - second single line string
#       idx   - index at which to indicate difference
#     Output:
#       Returns a three line formatted string showing the location
#       of the first difference between line1 and line2.

#       If either input line contains a newline or carriage return,
#       then returns an empty string.

#       If idx is not a valid index, then returns an empty string.
#     """
#     return ""


# def multiline_diff(lines1, lines2):
#     """
#     Inputs:
#       lines1 - list of single line strings
#       lines2 - list of single line strings
#     Output:
#       Returns a tuple containing the line number (starting from 0) and
#       the index in that line where the first difference between lines1
#       and lines2 occurs.

#       Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
#     """
#     return (IDENTICAL, IDENTICAL)


# def get_file_lines(filename):
#     """
#     Inputs:
#       filename - name of file to read
#     Output:
#       Returns a list of lines from the file named filename.  Each
#       line will be a single line string with no newline ('\n') or
#       return ('\r') characters.

#       If the file does not exist or is not readable, then the
#       behavior of this function is undefined.
#     """
#     return []


# def file_diff_format(filename1, filename2):
    # """
    # Inputs:
    #   filename1 - name of first file
    #   filename2 - name of second file
    # Output:
    #   Returns a four line string showing the location of the first
    #   difference between the two files named by the inputs.

    #   If the files are identical, the function instead returns the
    #   string "No differences\n".

    #   If either file does not exist or is not readable, then the
    #   behavior of this function is undefined.
    # """
    # return ""