import random
# Program returns integers in reverse order within 32-bits
# The approach I took with this is to convert the ints to string and iterate over them in reverse order
# Then I returned them back into ints to check to make sure they are within the bit limit


def reverint(x):
    valid = False
    numbers = str(x)
    lis = [numbers[y] for y in reversed(range(0, len(numbers)))]
    
    # this is a short case if there is a negative detected in the input
    if "-" in lis:
        
        for item in lis:

            if item == "-":
                lis.remove("-")
                z = "".join(lis)
                nums = int(z) * -1

    else:
        z = "".join(lis)
        nums = int(z)

    if nums <= 2**31 and nums >= -2**31:
        valid = True

    else:
        valid = False

    if valid == True:
        return nums

    if valid == False:
        return 0
    
print(reverint(random.randint(-2147483648, 2147483648)))