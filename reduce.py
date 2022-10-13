import json
from copy import deepcopy

FILE = 'county.geo.json'
FILED_TO_KEEP = [
    "STATEFP10",
    "COUNTYFP10",
    "GEOID10",
    "NAME10",
    "NAMELSAD10",
    "INTPTLAT10",
    "INTPTLON10",
    "state",
]

json_file = json.load(open(FILE))
reduced_json_file = deepcopy(json_file)

for idx, e in enumerate(json_file["features"]):
    print(idx)
    for k in e["properties"].keys():
        if k not in FILED_TO_KEEP:
            del reduced_json_file["features"][idx]["properties"][k]

with open(f"reduced.{FILE}", "w+") as f:
    json.dump(reduced_json_file, f)