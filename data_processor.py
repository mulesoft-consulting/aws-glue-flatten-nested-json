import json 

def convert_struct_to_str(datum):
    fields = list(datum.keys())
    fields.remove("Tags")
    for field in fields:
        datum[field] = str(datum[field]).replace("'", '"')
file_name = "s3://cloud-governance-outputs/427000243349/us-east-1/ec2-tagging/2022/02/05/04/resources.json.gz"
arr_fn = file_name.split("/", )
dest_bucket_name = "processing-bucket"
dest_file_path = arr_fn[0]+"/"+arr_fn[1]+"/"+dest_bucket_name+"/"+arr_fn[5]+"/"+arr_fn[6]+"/"+arr_fn[7]+"/"+arr_fn[8]+"/"+arr_fn[9]+"/"+arr_fn[3]+"/"+arr_fn[4]+"/"+arr_fn[10]
f = open(file_name)
data = json.load(f)
for datum in data["resources"]:
    convert_struct_to_str(datum)

with open(dest_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)