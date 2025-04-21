def read_and_write_file():
  try:
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read from: ")
    
    # Attempt to open and read the input file
    with open(input_file, 'r') as file:
      content = file.readlines()
    
    # Modify the content (example: add line numbers)
    modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
    
    # Ask the user for the output file name
    output_file = input("Enter the name of the file to write to: ")
    
    # Write the modified content to the output file
    with open(output_file, 'w') as file:
      file.writelines(modified_content)
    
    print(f"Content successfully written to {output_file}")
  
  except FileNotFoundError:
    print("Error: The file does not exist.")
  except IOError:
    print("Error: An error occurred while reading or writing the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
  read_and_write_file()