#site_name = "power learn project"
#print(site_name)

#Assigning a new value to site_name
#site_name = "I love coding"
#print(site_name)

#num1 = 5
#num2 = 5.3
#print(type(num1))
#print(type(num2))

# name = "Dodge Challenger"

# age = 4

# print(name)
# print(age)
# print("My car's age is", age)
# print(type(name))


#Tuples
#products = ('Xbox', 499.99, "Habibi", 23)
#print(products)

#mylist = ['p', 'r', 'o', 'g', 'r', 'a', 'm','i']
#print(mylist[5:])  # Output: ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i']

# name = 'DODGE CHALLENGER'
# age = 5
# owner = 'Dennis'
# location = 'Kenya'
# print(f"This car, the {name} is {age} years old, owned by {owner} who lives in {location}.")




#Open a specific file and which mode to open in / Create a new file and write to it
file = open('input.txt','w')
data = ('Hello, World!\n'*5)
file.write(data)

# Reading a file
file = open('input.txt', 'r')
data = file.read()
print(data)

#Counts the number of words in the file
word_count = len(data)

#Converts all text to uppercase
file = open('input.txt','w')
data = ('Hello, World!\n'*5)
file.write(data.upper())

#Reading the modified/processed file
file = open('input.txt', 'r')
data = file.read()
print(data)
print(f"Word count: {word_count}")  #Prints the word count in the file

#Writing the processed data to a new file named output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(f"Original Data:\n{data}\n")
    outfile.write(f"Word Count: {word_count}\n")

print(f"Successfully written processed text from input.txt to output.txt")


# Error handling with try-except
# file =  open('newFile.pdf', 'r')
# content = file.read()
# print(content)

# try:
#     file =  open('newFile', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("File operation completed")
#     file.close()

# try:
#     file = open("jsMummies_Contacts.pdf", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found. Please check the file path.")













