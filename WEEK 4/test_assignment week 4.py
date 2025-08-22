# Reading from a file with error handling and user input
while True:
    filename = input('assignment_input.txt')
    try:
        with open('assignment_input.txt', "r") as file:            # Attempt to open the file for reading
            data = file.read()
        print(f"Successfully read assignment_input.txt:")
        print(data)
        break                                        #Exit loop after successful read
    except FileNotFoundError:
        print(f"File not found. Please check the file path.")
    except PermissionError:
        print(f"You do not have permission to access this file.")
    finally:
            print("File operation completed")