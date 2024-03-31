list1 = [[1, 2], [3, 4]]
list2 = [[1, 2], [3, 4]]  # Different object creation
list3 = list1  # Assigning reference

print(list1 is list2)  # False: Equivalent structure, distinct memory locations
print(list1[0] is list2[0])  # False: Individual elements might also be distinct
print(list1 is list3)  # True: Identical (same reference)

string1 = "Hello"
string2 = "Hello"  # String literals often point to same object in memory
string3 = string1[:]  # Slicing creates a new string object

print(string1 is string2)  # True: Often identical for string literals
print(string1 is string3)  # False: Slicing creates a new object

def modify_mutable_list(list_arg: list) -> list:
    new_list = list_arg.copy()  # Explicitly create a copy to avoid modifying original
    new_list.insert(0, "apple")
    return new_list

my_list = [1, 2, 3]
modified_list = modify_mutable_list(my_list)
print(my_list)  # Output: [1, 2, 3] (Original remains unchanged)
print(modified_list)  # Output: ["apple", 1, 2, 3]