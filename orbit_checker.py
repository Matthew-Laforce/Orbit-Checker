""" ============================================================================

MATH 322 -- Assignment 3 -- Q5 Orbit Checker
Matthew Laforce
Created Jan 28, 2025

============================================================================ """

# Insert the orbit and the value for 'n' here
orbit = [1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18]
n = 23

# Create a new list containing all differences between orbit values
orbit_differences = []
orbit_size = len(orbit)
for value in range(orbit_size):
    for comparison in range(orbit_size):
        # Compare all values (mod size); append all non-zeroes to the list
        if value != comparison:
            orbit_differences.append((orbit[value] - orbit[comparison]) % n)

# Output the results
print(f"Results: {orbit_differences}")
sorted_list = sorted(orbit_differences)
print(f"Sorted : {sorted_list}")

# Find the largest number of possible matches (lambda)
max_matches = 0
index = 0
while index < len(orbit_differences):
    compare_count = 0
    temp_lambda = 0
    while compare_count < len(orbit_differences):
        if orbit_differences[compare_count] == orbit_differences[index]:
            temp_lambda += 1
        compare_count += 1
    if temp_lambda > max_matches:
        max_matches = temp_lambda
    index += 1
    
print(f"Lambda = {max_matches}")