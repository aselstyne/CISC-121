# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Start with the given binary_string function

def binary_string(n):
   '''parameter:
         n - integer
         
      returns a string of "0"s and "1"s giving the binary representation of n
      returns None if n is not an integer
   '''
   
   if type(n) is not int:
      return None
   else:
      if n == 0:
         return '0'
      else:
         negative = (n < 0)
         n = abs(n)
         bin_string = ''
         while n != 0:
            if n % 2 == 1:
               bin_string = '1' + bin_string
            else:
               bin_string = '0' + bin_string
            n = n // 2
         if negative:
            bin_string = '-' + bin_string
         return  bin_string  

def test_basic_int():
    '''Tests for correctness when using a basic integer as input'''
    assert binary_string(2) == '10'

def test_float():
    '''Tests a floating point number'''
    assert binary_string(10.8) == None

def test_8_bit():
    '''Tests a bigger number to ensure consistency'''
    assert binary_string(255) == '11111111'

def test_negative():
    '''Tests the sign using a negative number'''
    assert binary_string(-2) == '-10'