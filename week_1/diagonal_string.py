


def diagonal(string):

    # iterating each charater one by one, the spaces will be added by +2 so the character moves to forward with newline
    # creating diagonal.

    spaces = 0

    for s in string:
        print(' ' * spaces + s)
        spaces += 2



diagonal('Huzaifa')