import json 

def convert_struct_to_str(datum):
    fields = list(datum.keys())
    fields.remove("tags")
    for field in fields:
        datum[field] = str(datum[field]).replace("'", '"')


def process_column_name(col_name):
    words = []
    start_index = 0
    for i in range(len(col_name)):
        if col_name[i].isupper():
            if start_index != i:
                words.append(col_name[start_index:i].replace(":","").replace("-", "_").lower())
                start_index = i
    words.append(col_name[start_index:].lower())
    if len(words) > 1:
        return "_".join(words)
    else:
        return words[0]


def process_column_names(data):
    data_to_return = data

    if type(data) == dict:
        data_to_return = {process_column_name(k): v for k,v in data.items()}
        for k,v in data_to_return.items():
            data_to_return[k] = process_column_names(v)

    if type(data) == list:
        data_to_return = []
        for datum in data:
            data_to_return.append(process_column_names(datum))

    return data_to_return

f = open("instances.json")
data = json.load(f)
processed_data = process_column_names(data)
for datum in processed_data["resources"]:
    convert_struct_to_str(datum)

with open("new_resources.json", "w", encoding="utf-8") as f:
    json.dump(processed_data, f, ensure_ascii=False, indent=4)