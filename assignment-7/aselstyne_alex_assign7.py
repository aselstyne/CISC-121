'''
   CISC-121 2021F Section 001 - Assignment 7
   K-means clustering with zoo animals
   
   Alex Aselstyne
'''

# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity


import numpy as np
import random as rand

def manhatten(point1, point2):
    ''' Calculates the Manhatten metric between two points
    params: point1 and point2, two numpy arrays of coordinates
    returns: Manhatten metric for point1 and point2'''
    dist = 0
    for i in range(point1.shape[0]):
        dist += np.abs(point1[i]-point2[i])
    return dist

def euclid(point1, point2):
    ''' Calculates the Euclidean distance between two points
    params: point1 and point2, two NumPy arrays of coordinates
    returns: Euclidean distance between point1 and point2'''
    dist = 0
    for i in range(point1.shape[0]):
        dist += np.power(point1[i]-point2[i], 2)
    dist = np.sqrt(dist)
    return dist

def run_k_means(dist_algor, start_centers, points, labels, num_clusters):
    ''' Runs the k-means clustering algorithm on a data set, and gets the
    result ready to be printed out.
    params: dist_algor: the name of the distance algorithm to be used. Must be
                        the name of a function.
            start_centers: the centers for the algorithm to start with
            points: NumPy array of data points to be used in the calculations
            labels: labels for every index of the points array, for output
            num_clusters: number of clusters to be made
    returns: A 2D array of the labels grouped by cluster, and an array of 
            the number of points in each cluster. Both are used in printing'''

    num_rows = points.shape[0]
    num_cols = points.shape[1]
    # These variables are initialized for the 1st iteration of the while loop
    centers = start_centers
    unstable = True
    num_iters = 0
    while unstable:
        sum_of_points = np.zeros((num_clusters, num_cols)) 
        # REMINDER: num_points_by_cluster is the number of points in each
        # cluster, while cluster_for_points has related indecies for
        num_points_by_cluster = np.zeros(num_clusters, dtype=int)
        cluster_for_points = np.zeros(num_rows, dtype=int)

        # Now we loop through all the points, finding the closest cluster
        for p in range(num_rows):
            # Assign each animal a cluster number based on closest distance
            smallest_dist = dist_algor(points[p], centers[0])
            # Iterate through all centers to find the closest one
            for c in range(1, num_clusters):
                dist_to_c = dist_algor(points[p], centers[c])
                if dist_to_c < smallest_dist:
                    smallest_dist = dist_to_c
                    cluster_for_points[p] = c
            # Add the columns to the sum array, to find the avg point later
            sum_of_points[cluster_for_points[p]] += points[p]
            num_points_by_cluster[cluster_for_points[p]] += 1


        # Assign a new cluster center using the average of each column
        new_centers = np.zeros(centers.shape)
        # Divide every array of summed values by the number of points in that
        # cluster, so that you get the average point, or the new center.
        for clust in range(num_clusters):
            new_centers[clust] = sum_of_points[clust]/num_points_by_cluster[clust]
            
        # Now we check how far each center has moved, and store the max
        max_center_change = 0
        for i in range(num_clusters):
            center_change = dist_algor(centers[i], new_centers[i])
            if center_change > max_center_change:
                max_center_change = center_change
            
        
        # To get out of this loop, we check the stability conditions
        if num_iters == num_rows:
            unstable = False
        elif max_center_change < 0.1:
            unstable = False
        else:
            num_iters += 1
            centers = new_centers

    # Finally, prepare the data to be printed
    output = []
    for i in range(num_clusters):
        # Creates a list of 7 empty lists
        output.append([])
    for i in range(num_rows):
        # Populate each empty list with the names of the animals in that clust
        output[cluster_for_points[i]].append(labels[i])

    return output, num_points_by_cluster



zoo_attribs = np.loadtxt("C:\\Users\\Alexa\\Documents\\SCHOOL\\FIRST YEAR(2021-2022)\\CISC 121 - Intro to Comp Sci I\\Repo\\assignment-7\\zoo_2.txt", usecols = range(1,16), skiprows=1, dtype = int)
zoo_names = np.loadtxt("C:\\Users\\Alexa\\Documents\\SCHOOL\\FIRST YEAR(2021-2022)\\CISC 121 - Intro to Comp Sci I\\Repo\\assignment-7\\zoo_2.txt", usecols = 0, skiprows=1, dtype = str)
num_groups = 7

# This loop runs 10 times, for 10 different trials.
for run in range(10):
    # Choose the starting centers for this round
    start_centers = []
    for i in range(num_groups):
        start_centers.append(zoo_attribs[rand.randint(0, zoo_attribs.shape[0]-1)])
    
    # Do k-means algorithm and get the results using the manhatten metric
    animal_name_output, num_animals_in_cluster = run_k_means(manhatten, np.array(start_centers), zoo_attribs, zoo_names, num_groups)
    # Now display results:
    print('\nManhatten run number', run+1, 'results: ')
    for i in range(num_groups):
        print(i, ':', num_animals_in_cluster[i], 'animals, which are:', animal_name_output[i])
    
    # Now do the same thing with the the Euclidean algorithm
    animal_name_output, num_animals_in_cluster = run_k_means(euclid, np.array(start_centers), zoo_attribs, zoo_names, num_groups)
    print('\nEuclid run number', run+1, 'results: ')
    for i in range(num_groups):
        print(i, ':', num_animals_in_cluster[i], 'animals, which are:', animal_name_output[i])