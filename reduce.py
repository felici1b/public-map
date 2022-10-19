import json
from copy import deepcopy

INPUT_FILE_NAME = 'county.geo.json'
OUTPUT_FILE_NAME = 'county.reduced.geo.json'

FIELED_TO_KEEP = [
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
#LAT = []
#LONG = []

STATES = []

json_file = json.load(open(INPUT_FILE_NAME))

reduced_json_file = {
    "type": "FeatureCollection",
    "features": []
}


def is_filtered(e):
    cond_coord = len(LAT) == 0 or (LAT[0] < float(e["properties"]["INTPTLAT10"]) < LAT[1] and LONG[0] < float(e["properties"]["INTPTLON10"]) < LONG[1])
    cond_state = len(STATES) == 0 or e["properties"]["state"] in STATES
    return cond_state and cond_coord


for e in json_file["features"]:
    e_reduced = deepcopy(e)
    for k in e["properties"].keys():
        if k not in FIELED_TO_KEEP:
            del e_reduced["properties"][k]

    if is_filtered(e):
        reduced_json_file["features"].append(e_reduced)

with open(OUTPUT_FILE_NAME, "w+") as f:
    json.dump(reduced_json_file, f, separators=(',', ':'))
