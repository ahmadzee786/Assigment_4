

text_writing = input("Enter text to write to the file: ")
with open("Output.txt","w") as fi:
    fi.write(text_writing + "\n")
    print("Data successfully written to output.txt.\n\n")

    text_to_appending = input("Enter additional text to append: ")
with open("Output.txt","a") as fi:
 fi.write(text_to_appending + "\n")
print("Data successfully appended.\n\n")

print("\nFinal content of Output.txt:")
with open("Output.txt","r") as fi:
    content = fi.read()
    print(content)