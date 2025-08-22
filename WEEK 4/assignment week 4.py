#Open a specific file and which mode to open in / Create a new file and write to it
file = open('assignment_input.txt','w')
data = ('PLP, World!\n'*5)
file.write(data)

# Reading a file
file = open('assignment_input.txt', 'r')
data = file.read()
print(data)

# Appending content to a file
file = open('assignment_input.txt', 'a')
file.write("I am glad to be in the PLP program.")

#Reading the appended file
file = open('assignment_input.txt', 'r')
data = file.read()
print(data)

#Writing the processed data to a new file named assignment_output.txt
with open('assignment_output.txt', 'w') as outfile:
    outfile.write(f"Original Data:\n{data}\n")

print(f"Successfully written processed text from assignment_input.txt to assignment_output.txt")

# Error handling with try-except
def get_and_read_filename():
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, "r") as file:            # Attempt to open the file for reading
                data = file.read()
            print(f"Successfully read {filename}:")
            print(data)
            break                                        #Exit loop after successful read
        except FileNotFoundError:
            print(f"File not found. Please check the file path.")
        except PermissionError:
            print(f"You do not have permission to access this file.")
        finally:
            print("File operation completed")









































