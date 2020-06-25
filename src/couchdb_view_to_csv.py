import json
import csv

f = open("data/view.json", "rt")
data = json.loads(f.read())

f = open("data/view.csv", "w", newline="")
writer = csv.DictWriter(f, data["rows"][0].keys())
writer.writerows(data["rows"])
f.close()
