'''
   CISC-121 2021F Section 001 - Assignment 5
   Sorting algorithm efficiency comparison
   
   Alex Aselstyne
'''

# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

from matplotlib import pyplot as plt

def lotka(k_1, k_2, k_3, k_4):
    ''' Calculates Lotka-Volterra predetor prey equations
    params: The 4 constants used in the equations
    returns two lists, with populations of each species'''
    sheep = 100
    hyenas = 25
    num_years = 10000
    list_of_sheep_pops = [sheep]
    list_of_hyena_pops = [hyenas]
    for i in range(num_years):
        delta_s = k_1*sheep - k_2*sheep*hyenas
        delta_h = k_3*sheep*hyenas - k_4*hyenas
        sheep += delta_s
        hyenas += delta_h
        list_of_sheep_pops.append(sheep)
        list_of_hyena_pops.append(hyenas)
    return list_of_sheep_pops, list_of_hyena_pops

# Lotka-Volterra calculations
sheep_pops, hyena_pops = lotka(0.005, 0.0009, 0.0005, 0.02)
sheep_pops, hyena_pops = lotka(0.01, 0.0001, 0.0002, 0.03)


# Graph The Results
fig = plt.figure(figsize= (20,8))
fig.suptitle("Sheep Population vs Hyena Population")
plt.plot(sheep_pops, label = "Sheep population")
plt.plot(hyena_pops, label="Hyena Population")
plt.legend()
plt.show()