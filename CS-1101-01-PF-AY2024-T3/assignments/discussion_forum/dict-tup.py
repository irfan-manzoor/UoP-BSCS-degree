# 1. Looping through Lists with zip function:
# Sample data
names = ["Arfan", "Adnan", "Aadil"]
ages = [42, 40, 30]

# Looping with zip:
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# 2. Looping with Dictionary items method:
# Sample data
person = {"name": "Arfan", "age": 42, "city": "Lahore"}

# Looping with items:
for key, value in person.items():
    print(f"{key}: {value}")

# 3. Looping with enumerate function:
# Sample data
countries = ["Pakistan", "United Kingdom", "United States"]

# Looping with enumerate:
for index, country in enumerate(countries):
    print(f"{index+1}. {country}")
