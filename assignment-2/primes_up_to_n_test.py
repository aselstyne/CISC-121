# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Start with the given primes_up_to_n function

def primes_up_to_n(n):
   '''parameter :
          n - integer
          
   returns a list of all primes <= n
   returns None if n is not an integer
   '''
   if type(n) is not int:
      return None
   else:
      list_of_primes = []
      for potential_prime in range(2,n+1):
         #print("potential prime",potential_prime)
         could_be_prime = True
         done = False
         possible_divisor = 2
         while could_be_prime and possible_divisor < potential_prime:
            #print("\tpossible divisor",possible_divisor)
            if potential_prime % possible_divisor == 0:
               could_be_prime = False
               is_prime = False
            else:
               possible_divisor += 1
               
         if possible_divisor == potential_prime:
            list_of_primes.append(potential_prime)
            
      return list_of_primes

# Pytest functions:
def test_basic_number():
    '''Tests the base case with a straightforward number'''
    assert primes_up_to_n(10) == [2,3,5,7]

def test_negative_number():
    '''Tests a negative number as the input, which should give an empty
    list as there are infinite solution'''
    assert primes_up_to_n(-10) == []

def test_float():
    '''Tests a floating point number instead of an int'''
    assert primes_up_to_n(10.5) == None

def test_very_small():
    '''Tests the smallest prime, 2'''
    assert primes_up_to_n(2) == [2]