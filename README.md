# File-Handling-and-Exception
# 📝 File Read & Write with Error Handling

This Python program reads content from a user-specified file, modifies the content by adding line numbers, and writes the result to a new file. It includes basic error handling to manage issues like missing files or read/write errors.

It’s perfect for learning:
- File input/output (I/O)
- Exception handling
- Basic string and list operations

How It Works

1. The user is prompted to enter the name of an existing file to read from.
2. The program attempts to open and read this file.
3. It processes the content by adding line numbers to each line.
4. The user is then asked to specify the name of the output file.
5. The modified content is written to the new file.
6. Errors like "file not found" or "I/O issues" are handled with appropriate messages.



How to Use
1. Run the program.
2. Enter the name of the input file when prompted.
3. Enter the name of the output file to save the modified content.

Features
- Adds line numbers to each line in the input file.
- Handles file not found and I/O errors gracefully.
- Lets the user choose both input and output files.

Requirements
- Python 3

Example
Enter the name of the file to read from: notes.txt
Enter the name of the file to write to: numbered_notes.txt
Content successfully written to numbered_notes.txt