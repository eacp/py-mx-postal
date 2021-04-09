import pandas as pd
import json

print("reading data")

df = pd.read_csv("mx.csv")
groups = df.groupby("cp")

print("Grouping data")

mx = {}
for postal, group in groups:

	# Get the common data that is valid for the whole postal code
	data = group[['cp','municipio', 'ciudad', 'estado']].to_dict("records")[0]

	# Data specific to the areas (colonias, barrios, fraccs, pueblos)

	types = group["tipo"]
	areas = group["area"]

	data["areas"] = [ {'name': name, 'type': typ} for name, typ in zip(areas,types)]

	# add it to the general set

	mx[postal] = data

	# Export to individual file (like 100k files lol)
	with open(f"cps/{postal}.json", 'w') as individual:
		json.dump(data, individual)


# Write the whole data in JSON

with open("mx.json", 'w') as export:
	json.dump(mx, export)