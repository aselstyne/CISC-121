# Name:   Alex Aselstyne
# Student Number: 20289805
# Email:  alex.aselstyne@queensu.ca

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

''' This program will prompt the user for a folder of text files,
    then calculate the jaccard similarity values for all of the text files
    and output the best matches.'''
import tkinter as tk
from tkinter.filedialog import askdirectory
import glob
from pathlib import Path

def after_button():
    '''Triggered when the button is hit, loads the file list.
    Calls the make_sets() function when file is successfully open'''
    global text_files
    data_directory = askdirectory()
    # Use glob to get the list of all files
    text_files = glob.glob(data_directory + "\\" + "*.txt")
    working = tk.Label(window, text = "Working...")
    working.grid(row = 1, column = 0)
    window.update()
    working.destroy()
    make_sets()

def make_sets():
    '''Turns files into an array of sets of words, one for each document.
    Returns a lists of sets, each set containing all the words from a doc
    Calls the calc_jaccard() function to calculate jaccard scores'''
    # Go through each file, and make a set of all non-stop words
    words = []
    times_per_word = {}
    for i in range(len(text_files)):
        # The first file wouldn't open with the default encoding, so I switched to 
        # UTF-8, as described here: https://bit.ly/3uPjFXx
        # That's also the encoding specified in the file itself.
        file = open(text_files[i], "r", encoding = "utf8")
        file_words = set()
        for line in file:
            line = line.lower()
            line_words = line.split()
            # This will strip all stop words and punctuation from this line.
            for wordNum in reversed(range(len(line_words))):
                # Make the word contain only letters, nothing else.
                for char in line_words[wordNum]:
                    if char.isalpha() == False:
                        line_words[wordNum] = line_words[wordNum].replace(char, "")
                # Check for and remove stop words
                if line_words[wordNum] in stop_words:
                    del line_words[wordNum]
                else:
                    #Now I update the number of times this word has been seen.
                    if line_words[wordNum] in times_per_word:
                        times_per_word[line_words[wordNum]] += 1
                    else:
                        times_per_word[line_words[wordNum]] = 1
            
            # Adds all non-stop words from this line to the file's words.
            file_words.update(line_words)
        file.close()

        # After all lines have been loaded, check the number of times for each.
        for word in times_per_word:
            if times_per_word[word] < 5:
                file_words.discard(word)

        words.append(file_words)
    calc_jaccard(words)

def calc_jaccard(words):
    '''Calculates all the jaccard similarities for the given list of sets
    Param: a list of sets, each set being the words from a file
    Outputs to global variables most_similar and jaccard_scores'''
    # I used global variables, as calc_jaccard doesn't return to anywhere
    global most_similar, jaccard_scores
    # Go through the documents, finding which one has the best similarity.
    for text_num in range(len(words)):
        highest_jaccard = 0
        best_yet = -1 # Keeps track of the index in words of the best text.
        for text2_num in range(len(words)):
            # This ensures we're not checking a list against itself.
            if text2_num != text_num:
                intersection = words[text_num].intersection(words[text2_num])
                union = words[text_num].union(words[text2_num])
                jaccard = len(intersection)/len(union)
                # Check if the new jaccard is the best yet.
                if jaccard > highest_jaccard:
                    highest_jaccard = jaccard
                    best_yet = text2_num
        most_similar.append(best_yet)
        jaccard_scores.append(jaccard)



# I'm initializing variables up here, to keep myself organized.
stop_words = set()
text_files = []
most_similar = [] # Indicies correspond to indecies in text_files.
jaccard_scores = []

# Load the stop_words.txt file into a set.
p = Path(__file__).with_name("stop_words.txt")
stop_words_file = p.open("r")
# Remove any excess characters, like \n.
for line in stop_words_file:
    stop_words.add(line.rstrip())
stop_words_file.close()

# Build UI, then prompt user for their folder.
window = tk.Tk()
window.title("Jaccard Similarity Text Files")
window.geometry("1200x800")
open_folder = tk.Button(window, text = "Click to Select Text File Folder", command = after_button)
open_folder.grid(row = 0, column = 0)
window.update()

# The loop is necessary to display results after the button is clicked.
while True:
    # Present results, as outlined.
    if len(most_similar) != 0:
        # Create column headers.
        open_folder.destroy()
        col_0_label = tk.Label(window, text = "The Story:", font = (None, 20))
        col_1_label = tk.Label(window, text = "Is Most Similar To:", font = (None, 20))
        col_0_label.grid(row = 0, column = 0)
        col_1_label.grid(row = 0, column = 2)
        # Add dividers to make it look nice
        divider = tk.Label(window, text = "|", font = (None, 20))
        divider.grid(row = 0, column = 1)
        horiz_line = tk.Label(window, text = "--------------------------------------------------")
        horiz_line2 = tk.Label(window, text = "--------------------------------------------------")
        horiz_line.grid(row = 1, column = 0)
        horiz_line2.grid(row = 1, column = 2)
        # Populate all data into the table.
        for pair in range(len(most_similar)):
            text1 = text_files[pair].split("\\")[1]
            text1_label = tk.Label(window, text = text1)
            text1_label.grid(row = pair+2, column = 0)
            text2 = text_files[most_similar[pair]].split("\\")[1]
            text2_label = tk.Label(window, text = text2)
            text2_label.grid(row = pair+2, column = 2)
            text3_label = tk.Label(window, text = jaccard_scores[pair])
            text3_label.grid(row = pair+2, column = 3)
            divider = tk.Label(window, text = "|")
            divider.grid(row = pair+2, column = 1)
        
        # Exit loop once results have ben shown
        window.update()
        break

    window.update()

# Allows data to continue being shown
window.mainloop()