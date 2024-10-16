apartmentBuilding = [
    ["Apt 101", "Apt 102", "Apt 103"], 
    ["Apt 201", "Apt 202", "Apt 203"], 
    ["Apt 301", "Apt 302", "Apt 303"]
]

# TODO: Update "Apt 202" to "Renovated Apt 202" in `apartmentBuilding

# Setup a Traversal
# Use enumerate() to fetch both index and value for each floor of `apartmentBuilding`
# If we see "Apt 202", we can use the index from enumerate to edit the 2D array `apartmentBuilding`

print_string = ""

for floors in apartmentBuilding:
    for index, apt_number in enumerate(floors):
        if apt_number == "Apt 202":
            floors[index] = "Renovated Apt 202"
            apt_number = "Renovated Apt 202"
        
        print_string += apt_number + ", "

print_string = print_string[:-2]
print(print_string) 
print("\n")       
print(apartmentBuilding)
        
