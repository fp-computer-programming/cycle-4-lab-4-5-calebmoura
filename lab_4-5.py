# Author: caleb moura

# Prompt first user for their first name
person1 = input("Enter your first name: ")

# Prompt second user for their first name
person2 = input("Enter your first name: ")

# Use format method to create output string
output_string = "Hello, {}. My name is {}.".format(person1, person2)

# Print output string
print(output_string)