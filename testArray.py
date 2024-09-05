def get_unique_elements(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements_set = set(input_list)
    # Convert the set back to a list
    unique_list = list(unique_elements_set)
    return unique_list

# Sample List
sample_list = [1, 2 , 3, 3, 3, 3, 4, 5]

# Get the unique list
unique_list = get_unique_elements(sample_list)

# Print the unique list
print("Unique List:", unique_list)
