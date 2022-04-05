# This program accepts one, two or three command-line arguments, converts them
# into numbers (originally they are strings) and prints the result of some
# mathematical operations using these arguments. If the command-line arguments
# are invalid, an error exit code is returned by the whole program to the
# operating system.

import sys

# the first element in 'sys.argv' (at index 0) is always the script file name;
# therefore look for the numbers starting with the second element (index 1)
if len(sys.argv) == 2:
    arg1 = int(sys.argv[1])
    if arg1 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error
    result = arg1 + 42 - 4
    print("Result of the function is: ", result)
elif len(sys.argv) == 3:
    arg1 = int(sys.argv[1])
    if arg1 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error
    arg2 = int(sys.argv[2])
    if arg2 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error
    result = arg1 + arg2 - 4
    print("Result of the function is: ", result)
elif len(sys.argv) == 4:
    arg1 = int(sys.argv[1])
    if arg1 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error
    arg2 = int(sys.argv[2])
    if arg2 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error # end with 1 to indicate error
    arg3 = int(sys.argv[3])
    if arg3 < 0:
        print("Sorry, expected non-negative integers")
        sys.exit(1) # end with 1 to indicate error
    result = arg1 + arg2 - arg3
    print("Result of the function is: ", result)
else:
    print("Invalid arguments - expected 1..3 non-negative integer numbers")
    sys.exit(1) # end with 1 to indicate error
