# File reading code from here:
# https://docs.python.org/3/tutorial/inputoutput.html
with open("in.txt") as in_file:
    s = in_file.read()

    print("Input string: " + s)

    # Remove all non-alphanumeric characters from here:
    # https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()

    print("Input string after pre-processing: " + s)

    # Find the index of the last character
    # we need to check. For odd-length words,
    # we do not need to check the middle character,
    # hence the use of integer division.
    end_id = len(s)//2

    # Take advantage of the fact that you
    # can use negative indices to iterate
    # from the end of a list in python
    for i in range(end_id):
        # Exit the moment we don't find a match
        if s[i] != s[-i-1]:
            print("No")
            raise SystemExit(0)

    print("Yes")

