my_list = []   # Create an empty list
print(my_list)


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)


my_list.insert(2, 15)  # Inserting an element at a specific position
print(my_list)


my_list2 = [50, 60, 70]
my_list.extend(my_list2)  # Extending the list with another list
print(my_list)


my_list.remove(70) # Removing an element
print(my_list)


my_list.sort() # Sorting the list in ascending order
print(my_list)


my_list.index(30)
print(f"Index of 30 in the list: {my_list.index(30)}")  # Finding the index of an element
