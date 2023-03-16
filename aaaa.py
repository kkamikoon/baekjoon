import json

with open("abcd.json", "w") as file_w:
    file_w.write(json.dumps([1,2,3,4]))
