# Problem Statement:
# 
#   a. Write a function that will print the times tables for a given
#     number from 1 to 10.
#     Sample output:
#       tables(4) should display
#          1 x 4 =  4
#          2 x 4 =  8
#          3 x 4 = 12
#          4 x 4 = 16
#          5 x 4 = 20
#          6 x 4 = 24
#          7 x 4 = 28
#          8 x 4 = 32
#          9 x 4 = 36
#         10 x 4 = 40

def tables(number):
    for factor in range(1,11):
        print '{:2} x {:2} = {:2}'.format(factor, number, factor * number)


# Problem Statement:
# 
# b. Write a function called fizzbizz that will print numbers from
#    1 to 100. For multiples of 3, it should print "fizz", for
#    multiples of 5, it should print "bizz" and for multiples of
#    15, it should print "fizzbizz".
#    Sample Output:
#    fizzbizz() should display
#    1
#    2
#    fizz
#    4
#    bizz
#    fizz
#    7
#    8
#    fizz
#    bizz
#    11
#    fizz
#    13
#    14
#    fizzbizz
#    16
#    17
#    .
#    .
#    .
#    .

def fizzbizz():
    for number in range(1,101):
        if number % 15 == 0:
            print "fizzbizz"
        elif number % 5 == 0:
            print "bizz"
        elif number % 3 == 0:
            print "fizz"
        else:
            print number
