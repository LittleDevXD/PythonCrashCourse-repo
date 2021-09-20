import json

file = './past30days_eq_data.json'
with open(file, encoding='utf-8') as f:
    data = json.load(f)

new_file = './past30days_eq_data_r.json'
with open(new_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)