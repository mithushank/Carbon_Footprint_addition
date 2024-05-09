import json

# Specify the path to the JSON file
json_file_path = "/Users/kovintharajanmithushan/SUTD_Intern/Intern_Codes/Stream_Learning/carbon_footprints//energy_global_grid.json"

# Open the JSON file
with open(json_file_path, 'r') as json_file:
    # Read the JSON data
    content_data = json.load(json_file)

# Now, `content_data` contains the loaded JSON content
print(content_data)  # Display the loaded JSON content
