'''
   CISC-121 2021F Section 001 - Assignment 4
   
   Alex Aselstyne
'''
# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Part 1

# For each of the non-recursive functions given here, create
# a recursive function that produces the same result


# Problem 1:

def exponent(x,y):
   terms = []
   while y >= 1:
      if y % 2 == 1:
         terms.append(1)
      else:
         terms.append(0)
      y = y // 2
   terms.reverse() 
   
   result = 1
   for t in terms:
      result *= result
      if t == 1:
         result = result * x
   return result

# example of use
print(exponent(2,6))

   
def exponent_rec(x, y):
   ''' Compute the value of x^y, where y is a positive int, using recursion'''
   # Just call the function with y-1 until you get to y=1, then return values
   if y == 1:
      return x
   else:
      return x*exponent_rec(x, y-1)

print(exponent_rec(2,6))
print()


# Problem 2:

def sublist_sum(a_list, target):
   ''' determine if list a_list has a consecutive sub-list that sums to target '''
   for start in range(len(a_list)):
      sum = 0
      for finish in range(start, len(a_list)):
         sum += a_list[finish]
         if sum == target:
            return True
   return False

# example of use
print(sublist_sum([4, 9, 3, 1, 7, 2, 4], 13))
# the result is True because of the consecutive sublist [9, 3, 1]

def sublist_sum_rec(a_list, target):
   '''Determine if list a_list has a consective sub-list that sums to target '''
   return do_sublist_sum(a_list, target, 0, 0, 0)

def do_sublist_sum(a_list, target, start, index, sum):
   ''' Does the recusive computation for the sublist problem '''
   length = len(a_list)
   if sum == target:
      return True
   else:
      if index >= length:
         # Check if start is less than the length of the list
         if start < length -1:
            # Start over with index one more than start and start += 1
            return do_sublist_sum(a_list, target, start+1, start+2, 0)
         # else return false
         else:
            return False
      else:
         # increase sum by the value at index, increase index by 1
         return do_sublist_sum(a_list, target, start, index+1, sum+a_list[index])

# Yet another example:
print(sublist_sum_rec([4, 9, 3, 1, 7, 2, 4], 13))
print()


# Problem 3:

def prime_factors(n):
   ''' print the prime factorization of n'''
   while n > 1:
      candidate = 2
      while candidate <= n:
         if n % candidate == 0:
            print(candidate, " ", end="")    # this prints without starting a new line - very useful!
            n = n / candidate
         else:
            candidate += 1
   print()
   
# example of use
prime_factors(145)

def prime_factors_rec(n):
   ''' Prints the prim factorization of n, using recusion '''
   print(do_prime_factors(n, 2))

def do_prime_factors (n, candidate):
   ''' Does the actual computation of the recusive prime factors '''
   if n <= 1:
      return ""
   elif n % candidate == 0:
      return str(candidate)+ "  " + do_prime_factors(n/candidate, candidate)
   else:
      return do_prime_factors(n, candidate + 1)

# Example of use:
prime_factors_rec(145)
print()


# Problem 4:

def matching_parentheses(a_string):
   ''' determine if string a_string contains properly
      matched parentheses (i.e. each right parenthesis
      is matched with an earlier left parenthesis) '''
   left_parens = 0
   right_parens = 0
   for c in a_string:
      if c == '(':
         left_parens += 1
      elif c == ')':
         right_parens += 1
         if right_parens > left_parens:
            return False
   return  (left_parens == right_parens)
      
# example of use   
print(matching_parentheses("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))      

def matching_parentheses_rec(a_string):
   ''' Given a string, the function will determine if parenthases are 
      properly matched, returning either True or False'''
   return do_parenth(a_string, 0, 0, 0)

def do_parenth(a_string, index, num_left, num_right):
   # Check if we've reached the end of the string
   if index == len(a_string):
      # Return true if there is an equal number of both
      if num_left == num_right:
         return True
      else:
         return False
   # Determine if the current index is an open bracket or close, or neither
   elif a_string[index] == "(":
      return do_parenth(a_string, index+1, num_left+1, num_right)
   elif a_string[index] == ")":
      if num_left < num_right:
         return False
      else:
         return do_parenth(a_string, index+1, num_left, num_right+1)
   else:
      return do_parenth(a_string, index+1, num_left, num_right)

# Example of using it:
print(matching_parentheses_rec("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))
print()


# Part 2:

# Each of these recursive functions is inefficient due to duplicated
# effort.  Improve them by storing the solutions to smaller problems that
# are needed repeatedly.
      
    
# Problem 5

def collatz_up_to_n(n):
   ''' print the Collatz Sequence for each value from 1 to n '''
   for i in range(n):
      collatz_rec(i+1)

def collatz_rec(n):
   ''' print the Collatz Sequence for a single integer '''
   print(n, " ", end="")
   if n == 1:
      print()
      return
   else:
      if n % 2 == 0:
         n = n // 2
      else:
         n = 3*n + 1
      collatz_rec(n)

# Example of use:
collatz_up_to_n(2)

def better_collatz_up_to_n(n):
   ''' This version of the Collatz algorithm keeps values to be more efficient.
      Parameter n is the value to do sequences up to. '''
   known_vals = {1:"1"}
   for i in range(n):
      known_vals = better_collatz_rec(i+1, known_vals)

def better_collatz_rec(n, dict):
   ''' Prints the Collatz Sequence for an integer, using previous values. '''
   if n in dict:
      print(dict[n])
      # The dictionary must always be returned so we can assign it at the end
      # back to the known_vals variable.
      return dict
   else:
      # This computes new, unknown values.
      print(str(n) + " ", end="")
      if n % 2 == 0:
         new_n = n // 2
      else:
         new_n = 3*n + 1
      dict[n] = str(n) +" "+ better_collatz_rec(new_n, dict)[new_n]
      return dict

# Test that bad boy:
better_collatz_up_to_n(2)
print()


# Problem 6

def count_routes(n):
   ''' returns the number of different ways a robot can move forward a total of n metres, when the
       robot can only take steps that go forward either 2 metres or 3 metres. '''
   if n <= 1:
      return 0
   elif n <= 3:
      return 1
   else:
      return count_routes(n-2) + count_routes(n-3)
      
# Example of use:
print(count_routes(25))

def better_count_routes(n):
   ''' This is an improved way of counting routes a robot could take to move n
    meters, only taking 2 or 3 meter steps'''
   return count_routes_with_dict(n, {0:0, 1:0, 2:1, 3:1})
   

def count_routes_with_dict(n, dict):
   ''' Recursive function that keeps track of previous values using a dictionary'''
   if n in dict:
      # Don't forget that dictionaries are passed by reference, so
      # All recursive calls will have the whole dictionary, no matter the order
      return dict[n]
   else:
      dict[n] = count_routes_with_dict(n-2, dict) + count_routes_with_dict(n-3, dict)
      return dict[n]

# Use:
print(better_count_routes(25))
print()


# Part 3

# Write non-recursive functions to produce the same results as these recursive functions

# Example: look back at the example at the very top of this assignment ... but imagine I've
# given you the recursive "product" function and asked you to write the non-recursive version.

# Problem 7

def binary_search(a_list, target):
   ''' returns the location of target in a_list if target is in a_list, returns -1 if target is not in a_list 
       a_list must be sorted prior to calling this function
   '''
   return binary_search_rec(a_list, target, 0, len(a_list)-1)

def binary_search_rec(a_list, target, first, last):
   if first > last:
      return -1
   else:
      mid = (first + last) // 2
      if a_list[mid] == target:
         return mid
      elif a_list[mid] > target:
         return binary_search_rec(a_list, target, first, mid-1)
      else:
         return binary_search_rec(a_list, target, mid+1, last)
         
# Example of use
print(binary_search([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))

def binary_search_iter(a_list, target):
   '''Searches through a_list using binary search, returns the index of target
      in the list. Returns -1 if target is not in the list
      a_list must be sorted before calling the function'''
   lower = 0
   upper = len(a_list)
   while True:
      # Pick our new index
      if upper > lower+1:
         index = (lower+upper)//2
      else: 
         # This is incase the last value we land on is the target
         if a_list[lower] == target:
            return lower
         else:
            return -1
      # Check if target, and if not set new bounds and call again
      if a_list[index] == target:
         return index
      elif a_list[index] > target:
         upper = index
      elif a_list[index] < target:
         lower = index

# Use of bin search iter:
print(binary_search_iter([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))
print()


# Problem 8

def gcd(a,b):
   ''' returns the greatest common divisor of a and b, which must be positive integers '''
   if b == 0:
      return a
   else:
      return gcd(b, a % b)
      
# Example of use
print(gcd(8,20))

def gcd_iter(a,b):
   ''' Returns the GCD of a and b, two positive integers '''
   while b>0:
      temp = a
      a = b
      b = temp % b
   return a

# One final function test
print(gcd_iter(8,20))