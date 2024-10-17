colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_dict = {}

# Loop through the color in colors
for color in colors:

    if color in color_dict:
        # If the colour we've landed on exists in color_dict, increase its value by 1
        color_dict[color] += 1    
    else:
        # Else the color doesn't exist in color_dict yet so we can set its value to 1
        color_dict[color] = 1

print(color_dict)
print("\n")

# SO IMPORTANT:

# The colour is they key        => Key = Unique identifier (Only 1 colour)
# The frequency is the value    => Value = Frequency of the Unique Identifier (Can appear more than once)

# Code above can also be written using the .get(Key, default) method

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_dict = {}

for color in colors:

    # Get the value of the color key if it exists
    # If it exists add 1 to its current value
    # If it doesn't exist it's default is set to 0 and we add 1
    color_dict[color] = color_dict.get(color, 0) + 1
print(color_dict)


# Time Complexity - O(n), because we iterate through the list once

# Dictionary access, setting a value + getting a value  = O(1)
# for loop iterating over each element in the list =    = O(n) 


# Hashmaps allow us to count in a time efficient manner