#
#       Tiny code samples from my first few months learning Python. Keep practicing!
#       Chris S
#
#######################################################################

mouse = """\
          (\-.
          / _`>
  _)     / _)=
 (      / _/
  `-.__(___)_
"""
print(mouse)



#######################################################################

# Take user input string, truncated to 50 chars, and run some method checks on it.

S = input("\nWhat string would you like to run methods against?\n\n")

if len(S) >= 51:   #if statement to handle strings longer than 50 char
    S = S[0:50]
    print("String was too long, so it was truncated \n")
    print("Brevity over brilliance...\n")
else:()

#run method checks:

print ('Has at least 1 ALPHANUMERIC character:', any(x.isalnum() for x in S))
print ('Has at least 1 LOWERCASE character:', any(x.islower() for x in S))
print ('Has at least 1 UPPERCASE character:', any(x.isupper() for x in S))
print ('Has at least 1 ALPHABETICAL character:', any(x.isalpha() for x in S))
print ('Has at least 1 DIGIT:', any(x.isdigit() for x in S))

input() #don't close automatically

################################################################################################
#   Creating a Program to Calculate the Value of a Hyundai Excel
################################################################################################
# Updated second-to-last bisect breakpoint to ‘2015’ from 2014 as the former
# incorrectly associated input of “2014” with an unknown value (1962-2014
# non-inclusive of 2014).

import bisect

year =  int(input("What year model of Hyundai's Excel would you like to estimate cost for? \n[ENTER YEAR]\n"))
print('Approximate current value of the Hyundai Excel (', year, ') is',
      ['impossible to estimate as there was no such model. \nExcel was first released in 1962. ',
       '$18,500', '$6,000', '$12,000', '$48,000',
       '$200,000', '$650,000', '$35,000,000', '$52,000,000',
       'not possible to estimate (years from future not calculable). \nPlease try another year.']
      [bisect.bisect([1962,1964,1968,1971,1975,1980,1985,2012,2015,99999999], year)])


################################################################################################
#    Repetition Control Structure – Floating Point Numbers
################################################################################################

# no revisions necessary                         #  User instruction v v v v

print ("For this application, you are requested to enter five (5) floating point real values.\n\n(Error handling will allow for retry if invalid input is received.)")

list_of_floats = []                              #  define list to catch entered values:

while True:                                      #  accept user input as float for FIRST ENTRY -- if not valid, retry:
    try:
        bfc = (float(input("\nPlease enter the first value now [NUMBERS ONLY PLEASE]: ")))  #bfc = buffer variable for float/int check
        break
    except ValueError:
        print("\nOops!  Your entry could not be stored as a float.  Try again...")

list_of_floats.append(bfc)                       #  append the verified float value to the end of our list


while len(list_of_floats) < 5:                   #  start while loop for REMAINDER of entries
    entries_left = 5 - len(list_of_floats)       #  countdown mechanism / loop exit control
    while True:                                  #  >>>>  input subloop, repeating above logic
        try:
            bfc = (float(input("\nPlease enter another float value (" + str(entries_left) + ' left): ')))
            break
        except ValueError:
            print("\nOops!  Your entry could not be stored as a float.  Try again...")
    list_of_floats.append(bfc)

input("\nAll done. Press [Enter] to run some calculations on the gathered data.")

#  Perform calculations on list:                 #  run required calculations, one by one for aesthetics

print ("\nTotal of entered values:", sum(list_of_floats), "[ENTER >> next]", end="", flush=True); input()
print ("\nAverage of entered values:", sum(list_of_floats) / len(list_of_floats), "[ENTER >> next]", end="", flush=True); input()
print ("\nMaximum entered value:", max(list_of_floats), "[ENTER >> next]", end="", flush=True); input()
print ("\nMinimum entered value:", min(list_of_floats), "[ENTER >> next]", end="", flush=True); input()
input("\nThat's all the operations we have. Press [Enter] to calculate interest-added values.")

#  Apply interest on values:

after_interest = [ x+0.2*x for x in list_of_floats]

print ("\nInterest_Value = Original_value + Original_value*0.2 =\n\n       ", after_interest); input()

input("All done!!")


#######################################################################
#           String concatenation and other operations
#######################################################################

# Per feedback, completely revised structure. Program now defines a method to neatly concatenate input values and reverse the resulting string.
# This method is then called from the main method on user input (three recorded strings).

def concatAndReverse(strings):           # function to concatenate and reverse strings
    return ''.join(strings)[::-1]        # ''.join(strings) concatenates input, [::-1] slices the result into characters and reverses their order

def main(given_strings=[]):              # define main method and summon a blank list simultaneously, saves from newlining ("given_strings = []")
    while len(given_strings) < 3:        # set limit of string collection to 3
        given_strings.append(str(input('\nPlease input string # {}: '.format(len(given_strings)+1)))) # input string values and store in list
    print("\nYour original strings: ", given_strings, "\n")          # show the user's input for comparison
    print("Concatenated + Reversed: ", concatAndReverse(given_strings), end="") #print the result

if __name__ == "__main__":               # use main method based on namespace
    main()
    input("\n\n")                        # wait


###################################################################
#        Python complex number calculator (learning classes)
###################################################################

# Added user prompt for what to enter and how.

#       Comments use the following shorthand for arithmetic:
#               x = first user entry
#               y = second user entry
#                   a = real part
#                   b = imaginary part

import math

class Complex(object):                                # define class to allow operating on complex numbers
    def __init__(self, real, imaginary):              # init method to define complex as two parts, real and imaginary:
        self.real = real                              # real part
        self.imaginary = imaginary                    # imag part

    def __add__(self, no):                            # method for handling addition
        real = self.real + no.real                    # add input reals together
        imaginary = self.imaginary + no.imaginary     # add input imags together
        return Complex(real, imaginary)               # combine results as single complex obj

    def __sub__(self, no):                            # method for handling subtraction
        real = self.real - no.real                    # subtract input2 real from input1 real
        imaginary = self.imaginary - no.imaginary     # subtract input2 imag from input1 imag
        return Complex(real, imaginary)               # combine results as single complex obj

    def __mul__(self, no):                                                  # mult method
        real = self.real * no.real - self.imaginary * no.imaginary          # calc real, per x.a * y.a - x.b * y.b;
        imaginary = self.real * no.imaginary + self.imaginary * no.real     # calc imag, per x.a * y.b + x.b * y.a;
        return Complex(real, imaginary)                                     # combine results as single complex obj

    def __truediv__(self, no):                        # handle division. __div__ was 2.x-only. Using __truediv__.
        x = float(no.real ** 2 + no.imaginary ** 2)   # mult DIVISOR(denominator) by CONJUGATE: (y.a + y.b) * (y.a - y.b) =  y.a^2 + y.a^2
        y = self * Complex(no.real, -no.imaginary)    # mult DIVIDEND(numerator) by CONJUGATE of DIVISOR: (x.a + x.b) * (y.a - y.b)
        real = y.real / x                             # get single real
        imaginary = y.imaginary / x                   # get single imag
        return Complex(real, imaginary)               # combine results to single complex obj

    def mod(self):                                              # handle calculating modulus
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)  # modulus of complex x + yi: sqrt(x^2 + y^2)
        return Complex(real, 0)                                 # combine results

    def __str__(self):                                          # define formatting for Complex instances.
        if self.imaginary == 0:                                 # handle negative/positive/zero input scenarios correctly:
            result = "{:.2f}+0.00i" .format(self.real)
        elif self.real == 0 and self.imaginary < 0:
            result = "0.0{:.2f}i" .format(self.imaginary)
        elif self.imaginary > 0:
            result = "{0:.2f}+{1:.2f}i" .format(self.real, self.imaginary)
        elif self.real == 0 and self.imaginary >= 0:
            result = "0.00+{:.2f}i" .format(self.imaginary)
        else:
            result = "{0:.2f}-{1:.2f}i" .format(self.real, abs(self.imaginary))  # use absolute value to prevent two minus signs display4 4
        return result

def main():                                      # define main function
    try:                                         # tuck everything in error handling wrapper
        C = map(float, input("\nInput your first number: ").split())          # input first entry as two floats "C", split into constituent part by default delimiter (space)
        D = map(float, input("\nAnd now the second: ").split())          # input second entry the same way as "D"
        x = Complex(*C)                          # our class takes variable arguments, so (*C) indicates to take unpack the Complex C as two args (real and imag)
        y = Complex(*D)                          # repeat process to declare var for second entry as a whole
        print ('\nRESULTS: (A + B, A - B, A x B, A / B, mod(A), mod(B)):\n')
        print ('\n\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))  # the magic. Use the math and str methods (as we manually defined them) on collected input.
    except ZeroDivisionError:                    # handle exception when divisor is zero
        print ("\nCANNOT DIVIDE BY ZERO. Try again with a different second entry:  \n")
        return main()                            # let user try again

    except TypeError:                            # handle exception when input line can't be split into exactly two parts
        print("\nEntry didn't meet the required [number][space][number] (ex: '5 4') format. Retry: \n")
        return main()

    except ValueError:                           # handle exception when non-numerical value entered
        print("\nSomething there wasn't a number. Try again: \n")
        return main()

print ("""Primitive Complex Number Calculator\n\n------------------\n\nPlease enter two complex numbers to perform arithmetic on.
\nInput two digits, separated by a space, on each line -- the first \nrepresenting the real part and the second the imaginary.
\nFOR EXAMPLE: input of '2 2' will be treated as '2 + 2i'\n\n------------------""")

if __name__ == "__main__":              # use main method based on namespace
    main()

input('\nThanks for using!\n\n') # wait
