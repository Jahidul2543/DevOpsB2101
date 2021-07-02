import json
import logging
from self import self

logging.basicConfig(filename='log/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
self.logger = logging.getLogger('urbanGUI')
"""
Deserializing JSON
JSON	--->    Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""


def read_json():
    logging.info('Read JSON file')
    with open("data/data.json", "r") as read_file:
        file_data = json.load(read_file)
        print(type(file_data))
        for k, v in file_data.items():
            print(k, v)

        president = file_data['president']
        print(president)
        print(type(president))
        age = president['age']
        print(type(age))
        hobby = president['hobby']
        print(hobby[0])
        print(json.dumps(president, indent=6))


def write_into_json_file():
    print('Write Into a JSON file')
    data = {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'age': 4, 'price': None, 'health': True, 'hobby': ['Cricket', 'Football', 'Cycling']}
    with open("data/my_file.json", "w") as write_file:
        json.dump(data, write_file)
        print(json.dumps(data, indent=4))


read_json()
write_into_json_file()
