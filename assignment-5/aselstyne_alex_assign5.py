'''
   CISC-121 2021F Section 001 - Assignment 5
   Sorting algorithm efficiency comparissson
   
   Alex Aselstyne
'''

# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

import time as t
import random as r

# Part 1: Implementation of radix sort.

def radix_sort(s):
    ''' Sorts a list using the radix sort algorithm
    param: s, list to be sorted
    returns a sorted version of the list'''
    sort_s = s[:] # Make a copy of the list so as not to destroy the original
    bucket = []
    # Create 9 empty lists in bucket
    for i in range(10):
        bucket.append([])

    # Loop through the sorting algorithm  
    i = 0
    while True:
        i += 1
        # Get each number in the bucket appropriate for it's digit
        for x in sort_s:
            d = (x%10**i)//10**(i-1)
            bucket[d].append(x)
        
        # Check if we have passed all the digits in our data set
        if len(bucket[0]) == len(s):
            break
        
        #Rebuild sort_s and reset bucket
        sort_s = []
        for digit in range(10):
            for value in bucket[digit]:
                sort_s.append(value)   
            bucket[digit] = []

    return sort_s


# Part 2: Implementation of Merge Sort:

def merge_sort(ls, start, end):
    ''' Sorts a list using the merge sort algorithm
    params: the list to be sorted, and the start and end values of the slice
    returns ls in sorted order.'''
    # Check for base case
    if start == end-1:
        return ls[start:end]
    
    # Else, return the two merged halves.
    mid = (end + start)//2
    merged_halves = merge(merge_sort(ls, start, mid), merge_sort(ls, mid, end))
    return merged_halves

def merge(ls1, ls2):
    ''' Merges two lists together in sorted order.
    params: the two lists to be merged together
    returns one list containing all values from the the original 2, sorted.'''
    pos1 = 0
    pos2 = 0
    final1 = len(ls1) - 1
    final2 = len(ls2) - 1
    result = []
    # Sort all of them until one list is empty
    while pos1 <= final1 and pos2 <= final2:
        if ls1[pos1] <= ls2[pos2]:
            result.append(ls1[pos1])
            pos1 += 1
        else:
            result.append(ls2[pos2])
            pos2 += 1
    # Extend with the rest of the other list
    if pos1 > final1:
        result.extend(ls2[pos2:])
    else:
        result.extend(ls1[pos1:])
    return result


# Part 3: Randomly generated lists

# Start with validity check:
for trial in range(100):
    unsorted_list = []
    # Append 100 random numbers to the list
    for i in range(100):
        unsorted_list.append(r.randint(0,1000))
    if merge_sort(unsorted_list, 0, 100) != radix_sort(unsorted_list):
        print("WHOA BIG MAN, WE HAVE AN ERROR")

# Now this is the efficiency check:
radix_times = []
merge_times = []
for trial in range(100):
    unsorted_list = []
    # Append 10000 random numbers to the list
    for i in range(10000):
        unsorted_list.append(r.randint(100000,999999))
    # Call each function, then store the time they take
    radix_start = t.time()
    radix_sort(unsorted_list)
    radix_end = t.time() # This is used for the start of merge sort, too.
    merge_sort(unsorted_list, 0, len(unsorted_list))
    merge_end = t.time()
    radix_times.append(radix_end - radix_start)
    merge_times.append(merge_end - radix_end)


# Part 4: Print the data
radix_wins = 0
merge_wins = 0
ties = 0
radix_avg = 0
merge_avg = 0
for i in range(len(radix_times)):
    radix_avg += radix_times[i]
    merge_avg += merge_times[i]
    if radix_times[i] > merge_times[i]:
        merge_wins += 1
    elif radix_times[i] < merge_times[i]:
        radix_wins += 1
    else:
        ties += 1

radix_avg = radix_avg/len(radix_times)
merge_avg = merge_avg/len(merge_times)

print("Radix was faster", radix_wins, "times.")
print("Merge sort was faster", merge_wins, "times.")
print("They tied", ties, "times.")
print("Radix averaged:", radix_avg,"  Merge sort averaged:", merge_avg)