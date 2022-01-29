# (line 3-4) File reading code from here:
# https://docs.python.org/3/tutorial/inputoutput.html
with open("in.txt", encoding='utf8') as in_file:
    s = in_file.read()

    print("Input string: " + s)

    # (line 10) Remove all non-alphanumeric characters from here:
    # https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()

    print("Input string after pre-processing: " + s)

    # Find the index of the last character
    # we need to check. For odd-length words,
    # we do not need to check the middle character,
    # hence the use of integer division.
    end_id = len(s)//2

    # Bool to tell whether the single allowed mistake
    # has been detected or not
    error_found = False

    # Adjustment variables to skip the mistake character
    # if it has been detected
    adj_start = 0
    adj_end = 0

    # Take advantage of the fact that you
    # can use negative indices to iterate
    # from the end of a list in python
    for i in range(end_id):
        # When a mismatch is found
        if s[i+adj_start] != s[-i-1-adj_end]:
            # If this is the first mistake
            if not error_found:
                error_found = True
                # Try the pairs made by skipping the
                # characters at either end and seeing
                # if a valid pair is formed
                if s[i+1] == s[-i-1]:
                    # record the character and its position
                    bad_string = s[i]
                    bad_id = i
                    # set the adjustment variable
                    adj_start = 1
                elif s[i] == s[-i-2]:
                    bad_string = s[-i-1]
                    bad_id = len(s)-i-1
                    adj_end = 1
                # If neither pair works, this is not
                # a palindrome
                else:
                    print("No")
                    raise SystemExit(0)
            else:
                print("No")
                raise SystemExit(0)

    # Different outputs depending on whether
    # a bad character was found or not
    if not error_found:
        print("Yes. Note: string itself is a palindrome and no need to delete.")
    else:
        print("Yes, delete " + bad_string + " at position " + str(bad_id))

