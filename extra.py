import json
import camelcase


simple_json = '{ "fname":"Shivam", "lname":"Kashyap" }'


map = json.loads(simple_json);

for x in map.values():
    print(x)



text = "shivam kashyap"

print(text)

print(camelcase.CamelCase().hump(text))