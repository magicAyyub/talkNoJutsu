from pathlib import Path
from src.settings import *
import json
from colorama import Fore, Style

def is_valid_line(line):
    if line.strip() == '':
        return False
    else:
        if line.strip().startswith('Name format'):
            return False
        else:
            return True
def format_line(line):
    return line.strip().split(' ')[-1]

def extract_data(line):
    parts = line.split('/')
    data_type = parts[0]
    language = parts[1]
    dataset = parts[2]
    model = parts[3]
    return data_type, language, dataset, model

# read the models_list.txt file
try:
    with open(BASE_DIR / '/out/models_list.txt', 'r') as file:
        raw_data = file.read()
except FileNotFoundError:
    print(Fore.RED +"Le fichier 'models_list.txt' n'existe pas." + Style.RESET_ALL)
    exit()
        
# Split the raw data into lines
lines = raw_data.strip().splitlines()
# Remove empty lines and lines that don't contain model names
lines = list(filter(is_valid_line, lines))
# Format the lines
lines = list(map(format_line, lines))


# Create an empty data structure
data_structure = {}

# Process each line
for line in lines:
    data_type, language, dataset, model = extract_data(line)
    # Check if the data type exists
    if data_type not in data_structure:
        data_structure[data_type] = {}
    # Check if the language exists
    if language not in data_structure[data_type]:
        data_structure[data_type][language] = {}
    # Check if the dataset exists
    if dataset not in data_structure[data_type][language]:
        data_structure[data_type][language][dataset] = []
    # Add the model to the dataset
    data_structure[data_type][language][dataset].append(model)


# Convert the data structure to JSON
json_structure = json.dumps(data_structure, indent=4, ensure_ascii=False)

# Save the JSON structure to a file
with open(BASE_DIR / '/out/structured_models.json', 'w') as json_file:
    json_file.write(json_structure)

# Print a success message
print(Fore.GREEN + "Les données ont été structurées et enregistrées dans 'out/structured_models.json'." + Style.RESET_ALL)
