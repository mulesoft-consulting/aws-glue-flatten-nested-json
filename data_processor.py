import json 

def convert_struct_to_str(datum):
    fields = list(datum.keys())
    fields.remove("tags")
    for field in fields:
        datum[field] = str(datum[field]).replace("'", '"')

# Helper function to convert a string from camel style to underscore separated
def process_column_name(col_name):
    words = []
    start_index = 0
    for i in range(len(col_name)):
        if col_name[i].isupper():
            if start_index != i:
                words.append(col_name[start_index:i].replace(":","").replace("-", "_").lower())
                start_index = i
    words.append(col_name[start_index:].replace(":","").replace("-", "_").lower())
    if len(words) > 1:
        return "_".join(words)
    else:
        return words[0]

# Recursively converts all field names from camel style to undersocre separated
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

file_name = "s3://cloud-governance-outputs/427000243349/us-east-1/ec2-tagging/2022/02/05/04/resources.json.gz"
arr_fn = file_name.split("/", )
dest_bucket_name = "processing-bucket"
dest_file_path = arr_fn[0]+"/"+arr_fn[1]+"/"+dest_bucket_name+"/"+arr_fn[5]+"/"+arr_fn[6]+"/"+arr_fn[7]+"/"+arr_fn[8]+"/"+arr_fn[9]+"/"+arr_fn[3]+"/"+arr_fn[4]+"/"+arr_fn[10]
f = open(file_name)
data = json.load(f)
processed_data = process_column_names(data)
for datum in processed_data["resources"]:
    convert_struct_to_str(datum)

with open(dest_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

