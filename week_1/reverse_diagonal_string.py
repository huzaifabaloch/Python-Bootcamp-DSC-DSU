

def reverse_diagonal(string):

    # Similarly this time I've taken lenght of entire string and multiplied by 2 and starting displaying character from end 
    # and subtracting -2 each character.
    
    spaces = len(string) * 2

    for s in string:
        print(' ' * spaces + s)
        spaces -= 2

reverse_diagonal('Huzaifa')