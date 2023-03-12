# Assignment 3 - File I/O and tkinter

For this assignment, we were to determine the [Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index) between different sets of words, read from text files. This data then had to be output using the `tkinter` builtin Python module.

The script I created will ask the user for a directory to load `.txt` files from, determine sets of words to represent each file (without [stop words](https://en.wikipedia.org/wiki/Stop_word)), and then calculate and display the similarity between each set. It uses `tkinter`'s grid layout to display the results.

The PyDoc documentation is also included with the script, as well as the stop word list and some example (public domain) texts.