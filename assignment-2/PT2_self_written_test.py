# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Create the all_odd_or_even function

def all_odd_or_even(*args):
    # Check that at least one argument was recieved
    if len(args) < 1:
        return False
    
    # The try-except trys to determine if we have odd or even ints
    try:
        mod_val = args[0]%2
    except:
        # Incase args[0] is not an int
        return False
    
    for i in args:
        # Check that all the arguments are ints
        if type(i) is not int:
            return False
        # Check if all the numbers are either odd or even
        if i%2 != mod_val:
            return False
        
    # If we get here, all tests passed
    return True

def test_all_even():
    '''Tests with all even numbers'''
    assert all_odd_or_even(2,4,6) == True

def test_all_odd():
    '''Tests with all odd numbers'''
    assert all_odd_or_even(1,3,5) == True

def test_mixed():
    '''Tests with a mix of odd and even'''
    assert all_odd_or_even(1,2,3,4,5) == False

def test_not_int():
    '''Tests with a float value'''
    assert all_odd_or_even(2.4,4,6) == False

def test_no_args():
    '''Tests with no arguments'''
    assert all_odd_or_even() == False