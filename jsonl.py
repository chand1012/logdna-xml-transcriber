import json

# obj_list can be string with newline delimiters
# or can be a python list object
def loads(obj_list):
    load_object = []
    final_object = []
    if type(obj_list)==str:
        for line in obj_list.splitlines():
            if line:
                load_object.append(line)
    else: 
        load_object = obj_list

    for obj in load_object:
        final_object.append(json.loads(obj))
    return final_object

# This only takes a list of dictionaries
# returns a newline delimited JSONL string
def dumps(dict_list):
    final_string = ''
    for obj in dict_list:
        final_string += f"{json.dump(obj)}\n"
    return final_string