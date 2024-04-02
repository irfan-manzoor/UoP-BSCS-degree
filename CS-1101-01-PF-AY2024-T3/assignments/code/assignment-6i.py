# Initial employee names
employee_names = ["Irfan Manzoor", "Adnan M. Ahmad", "Aadil M. Wali", "Rayaan Irfan", 
                  "Azlaan Ahmad", "Abdal Haadi", "Mutahira Arsalan", "Kahdeeja Mir", 
                  "Marium Khan", "Aliza Khan"]

# Create sub-lists with 5 names each
subList1 = employee_names[:5]  # First 5 names
subList2 = employee_names[5:]  # Remaining names

# Print sub-lists
print("Sub-List 1:")  # Header for sub-list 1
for name in subList1:
    print(name)  # Print each name in sub-list 1

print("\nSub-List 2:")  # Header for sub-list 2
for name in subList2:
    print(name)  # Print each name in sub-list 2

# Add new employee to subList2
subList2.append("Kriti Brown")  # Append "Kriti Brown" to sub-list 2
print("\nAmended Sub-List 2:")  # Header for amended sub-list 2
for name in subList2:
    print(name)  # Print each name in amended sub-list 2

# Remove second employee from subList1
subList1.pop(1)  # Remove element at index 1 (the second employee)
print("\nAmended Sub-List 1:")  # Header for amended sub-list 1
for name in subList1:
    print(name)  # Print each name in amended sub-list 1

# Merge sub-lists
merged_list = subList1 + subList2  # Concatenate sub-lists
print("\nMerged-List:")  # Header for merged list
for name in merged_list:
    print(name)  # Print each name in merged list

# Sample salary list (replace with actual salary data)
salary_list = [40000, 52000, 38000, 45000, 60000, 48000, 55000, 42000, 58000, 49000]

# Give 4% raise to each employee
for i in range(len(salary_list)):
    salary_list[i] *= 1.04  # Multiply each salary by 1.04 for a 4% increase

# Sort the salary list in descending order
salary_list.sort(reverse=True)

# Print the top 3 salaries
print("\nTop 3 Salaries:")  # Header for top 3 salaries
for i in range(3):
    print(f"{salary_list[i]:,.2f}")  # Print the top 3 salaries with 2 decimal places
