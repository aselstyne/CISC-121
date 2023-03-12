# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Start with the given independent function

def independent(list_a, list_b):
   '''
      We can say that two lists are independent if no value occupies the
      same position in both lists.  Independent lists are not
      required to have the same length.

         For example, [1,2] and [2,1,3] are independent, and
         [1,2,3]  and [4,2,'a'] are not independent.
         
      Parameters:
         list_a and list_b must be lists

      Returns True if list_a and list_b are independent, and
      returns False if they are not
   '''
   if type(list_a) is not list  or type(list_b) is not list:
      return False
   else:
      min_length = min(len(list_a), len(list_b))
      for i in range(min_length):
         if list_a[i] == list_b[i]:
            return False
      return True

# Pytest functions:
def test_basic_independent():
   '''Tests two completely different lists'''
   assert independent([1,0], [2,3]) == True

def test_basic_dependent():
   '''Pytest function that checks two of the same list'''
   assert independent([1,0],[1,0]) == False

def test_1_same():
   '''Tests two lists with just one element the same'''
   assert independent([1,2], [1,3]) == False

def test_sub_indep():
   '''Tests with multiple elements the same'''
   assert independent([1,2,5,3], [4,2,5,'a']) == False

def test_diff_order():
   '''Tests with same all the same numbers in a different order'''
   assert independent([2,1,4], [4,2,1]) == True

def test_repeated_dep():
   '''Tests with repeated values'''
   assert independent([2,2,4], [2,2,6]) == False