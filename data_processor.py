import json 

def convert_struct_to_str(datum):
    fields = list(datum.keys())
    fields.remove("Tags")
    for field in fields:
        datum[field] = str(datum[field])

f = open("instances.json")
data = json.load(f)
for datum in data["resources"]:
    convert_struct_to_str(datum)

with open("new_resources.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)