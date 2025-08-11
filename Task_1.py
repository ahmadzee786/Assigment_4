'''Write a Python program that 
    Opens and reads a text file named sample.txt
    Prints its content line by line
    Handles errors gracefully if the file does not exist.'''
 
try:
    with open ('Sample.txt',
               'r') as file_1:
                        reading_file1 = file_1.read()
                        print(reading_file1)
                        file_1.close()
except FileNotFoundError:
        print(" Error : The file 'Sample,txt'  not found.")

 