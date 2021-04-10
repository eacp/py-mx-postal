import json
from unidecode import unidecode

# Load all the files

from glob import glob

states = {}

for f_name in glob('public/cp/*.json'):
	# Open the file
	with open(f_name, 'r', encoding="utf-8") as pcjson:
		# print(pcjson.name)
		pc = json.load(pcjson)

	# Add leading zeroes
	code = pc['cp']
	pc['cp'] = f"{code:05d}"

	state = pc['estado']

	if state not in states:
		states[state] = [pc]
	else:
		states[state].append(pc)

# Replacements for long names
replacements = {
	'Baja California Sur': 'bcs',
	'Baja California': 'bc',
	'Ciudad de México': 'cdmx',
	'Coahuila de Zaragoza': 'coahuila',
	'Michoacán de Ocampo': 'michoacan',
	'Veracruz de Ignacio de la Llave': 'veracruz',
	'Nuevo León': 'nl'
}

for key, data in states.items():
	
	if key in replacements:
		key = replacements[key]
	else:
		key = unidecode(key.lower())
	
	with open(f"public/states/{key}.json", 'w', encoding="utf-8") as state_file:
		json.dump(data, state_file)
