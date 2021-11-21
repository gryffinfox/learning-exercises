# Calculation program was a simple exercise to practice function writing.
# Assignment: write a function and test cases so that:
# If a number is even, it returns the cube
# If it's odd, it returns the double
# At least 4 test cases

def number(a):
    if a % 2 == 0:                              # Number is even
        cube = a ** 3                           # Return cube (**3)
        return cube
    
    else:                                       # Number is odd                                  
        double = a * 2                          # Return double
        return double
    
if number(2) == 8:
    print("ok")
else:
    print("Nope")
    
if number(3) == 6:
    print("ok")
else:
    print("Nope")
    
if number(0) == 0:
    print("ok")
else:
    print("Nope")
    
if number(-3) == -6:
    print("ok")
else:
    print("Nope")
    
if number(4+1) == 10:
    print("ok")
else:
    print("Nope")
    
