# Problem 1: Reverse a String (2 methods)

# Method 1 → using loop

str = 'Hello, World!'
reversed_str = ''
for i in str:
    reversed_str = i + reversed_str
print("Reversed string using loop:", reversed_str)