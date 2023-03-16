'''
   CISC-121 2021F Section 001 - Assignment 8
   Classes using restaurants and customers
   
   Alex Aselstyne
'''

# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity
from functools import total_ordering

@total_ordering
class Assignment8():
   ''' Parent class of the Restuarant and Customer classes.
   Contain functions useful to both, and functions to be overridden.'''
   
   def __init__(self, name = "anonymous", conn_type = None):
      ''' Initializes an instance.
      params: name - the name of this instance.
               conn_type: the type of object that this one can connect to.'''
      self.__name = name
      self.__connections = []
      self.__valid_connection_type = conn_type
      self.__score = 0
      
   def __str__(self):
      ''' If cast as a string, the object's name will be returned.'''
      return self.__name 
      
   def add_connection(self, con):
      ''' Adds a connection to con, given that it's a valid object.'''
      if type(con) == self.__valid_connection_type:
         self.__connections.append(con)
   
   def get_connections(self):
      ''' Returns a list of all the connections this instance has.'''
      return self.__connections

   def get_num_connections(self):
      ''' Returns the number of connections this instance has.'''
      return len(self.__connections)
         
   def compute_score(self):
      ''' Meant as a template, should be overridden by subclasses.'''
      self.__score = 0

   def update_score(self, score):
      ''' Updates the score variable.'''
      self.__score = score
      
   def get_score(self):
      ''' Returns this instance's score.'''
      return self.__score
      
   def get_name(self):
      ''' Returns this instance's name.'''
      return self.__name 

   def __eq__(self, inst2):
      ''' Determines if two instances are equal.
      This can go in Assignment8 as it's the same for both subclasses.'''
      if self.get_score() == inst2.get_score():
         if self.get_name() == inst2.get_name():
            # Don't have to check for length of names, as it's implied by ==
            return True
      return False
   
   def __ne__(self, inst2):
      ''' Determines if two instances are not equal, or if they are different.
      This can go in Assignment8 as it's the same for both subclasses.'''
      if self.get_score() != inst2.get_score():
         return True
      elif self.get_name() != inst2.get_name():
         return True
      else:
         return False
   
   def __lt__(self, inst2):
      ''' Determines if self is less than inst2.
      This is meant to be overridden by the subclasses.'''
      if self.get_score() < inst2.get_score():
         return True
      else:
         return False
      
      
class Customer(Assignment8):
   ''' Class representing a customer, holding all necessary data.
   Extends Assignment8.'''
   def compute_score(self):
      ''' Computes the score for this customer instance.'''
      new_score = 0
      for i in self.get_connections():
         new_score += i.get_score()
      # The score only needs to be changed from 0 if we have a connection
      # Also stops division by 0
      if self.get_num_connections() > 0:
         new_score = new_score/self.get_num_connections()
         self.update_score(new_score)
   
   def __lt__(self, inst2):
      ''' Determines if this class is less than another instance.
      Compares scores and then names to find out which instance is less.'''
      if self.get_score() < inst2.get_score():
         return True
      elif self.get_score() == inst2.get_score():
         # In case of a score tie, look at the alphabet
         if self.get_name() > inst2.get_name():
            return True
      # All other cases:
      return False

    
class Restaurant(Assignment8):
   ''' Class representing a restaurant, holding all necessary data.
   Extends Assignment8.'''
   def compute_score(self):
      ''' Computes this restaurants score using its customers.'''
      new_score = 0
      for i in self.get_connections():
         new_score += i.get_num_connections()
      self.update_score(new_score)
   
   def __lt__(self, inst2):
      ''' Determines if this class is less than another instance.
      Compares scores, lengths, then names to find which instance is less.'''
      if self.get_score() < inst2.get_score():
         return True
      elif self.get_score() == inst2.get_score():
         # > is used here, as we actually need them to be opposite
         # alphabetical order so they are ranked right when they are reversed.
         if len(self.get_name()) > len(inst2.get_name()):
            return True
         elif len(self.get_name()) == len(inst2.get_name()):
            # In case of a tie in name lengths, look at alphabetical order
            if self.get_name() > inst2.get_name():
               return True
      # This is only reached if nothing else was true:
      return False




# Main:     
if __name__ == '__main__':
   # Read in the file
   with open('Customers and Restaurants 2.csv') as dataset_file:
      file_lines = []
      for line in dataset_file:
         file_lines.append(line.rstrip().split(','))

   # Create lists of our names and database
   restaurants = []
   for name in file_lines[0][1:]:
      restaurants.append(Restaurant(name, Customer))
   customers = []
   database = []
   for row in range(1, len(file_lines)):
      line = file_lines[row]
      customers.append(Customer(line[0], Restaurant))
      # Cycle through the data entries, and add connections
      for column in range(1, len(line)):
         if line[column] == '1':
            customers[row-1].add_connection(restaurants[column-1])
            restaurants[column-1].add_connection(customers[row-1])

   # Generate scores for all Customers and Restaurants:
   for rest in restaurants:
      rest.compute_score()
   
   for cust in customers:
      cust.compute_score()

   # Determine the ranking
   ranked_restuarants = sorted(restaurants, reverse=True)
   ranked_customers = sorted(customers, reverse = True)
   
   # Print the results:
   print("Top 10 Restuarants:")
   for i in range(10):
      print(str(i+1) + ': ' + str(ranked_restuarants[i]) + "\tScore: " + str(ranked_restuarants[i].get_score()))
   
   print("\n\nTop 10 Customers:")
   for i in range(10):
      print(str(i+1) + ': ' + str(ranked_customers[i]) + "\tScore: " + str(ranked_customers[i].get_score()))