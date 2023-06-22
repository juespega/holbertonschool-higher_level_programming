#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Load existing data from the file
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

# Add new arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, "add_item.json")
