"""
Turn Unreadable Json file into Readable file
"""
import json

file = 'eq_data_30_day_m1.json'
with open(file) as f:
    all_eq_dict = json.load(f)

readable_file = 'eq_data_30_day_m1_r.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_dict, f, indent=4)