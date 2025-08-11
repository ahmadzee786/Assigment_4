# Assigment_4
# Task 1
Step 1 : create a try: block
Step 2 : with open ('Sample.txt', 'r') as file_1:
Step 3 : open('Sample.txt', 'r') tries to open a file named Sample.txt in read mode ('r').
Step 4 : with statement is a file is automatically closed when the block exits (even if an exception happens).
Step 5 : as file_1 assigns the opened file object to the name file_1.
Step 6 : reading_file1 = file_1.read()
Step 7 : print(reading_file1)
Output : 
Reading file contents
Line 1 : This is sample text file
Line 2 : It contains multiple lines

# Task 2
Step 1 : Asks the user to type some text.
Step 2 : Whatever the user provide input will be stored in the variable text_writing as a string
Step 3 : Open a file named Output.txt in write mode ("w").
Step 4 : Write mode will erase any existing file content before writing new data.
Step 5 : fi.write(text_writing + "\n") writes the user’s input to the file, followed by a newline.
Step 6 : Prints confirmation that the data has been written.
Step 7 : The with statement automatically closes the file after the indented block ends.
Step 8 : Asks the user for another line of text to append.
Step 9 : Opens Output.txt in append mode ("a").
Step 10 : Append mode does not erase existing content; it adds new data at the end.
Step 11 : Writes the new text with a newline at the end.
Step 12 : Prints a message confirming that the text was appended.

 Output : 

Enter text to write to the file: Hello, python.
Data successfully written to output.txt.

Enter additional text to append: Learning File handling in python.
Data successfully appended.


Final content of Output.txt:
Hello, python.
Learning File handling in python.
