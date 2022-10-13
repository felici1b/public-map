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


LAT = [23, 50]
LONG = [-132, -64]

json_file = json.load(open(FILE))

reduced_json_file = {
    "type":"FeatureCollection",
    "features": []
}

for idx, e in enumerate(json_file["features"]):
    e_reduced = deepcopy(e)
    for k in e["properties"].keys():
        if k not in FILED_TO_KEEP:
            del e_reduced["properties"][k]

    if LAT[0] < float(e["properties"]["INTPTLAT10"]) < LAT[1] and LONG[0] < float(e["properties"]["INTPTLON10"]) < LONG[1]:
        reduced_json_file["features"].append(e_reduced)


with open(f"reduced.{FILE}", "w+") as f:
    json.dump(reduced_json_file, f)