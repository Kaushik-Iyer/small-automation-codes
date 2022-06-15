import sys
import clipboard
import json

saved_data='clipboard.json'
def save_items(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

def load_json(path):
    try:
     with open(path,'r') as f:
        data=json.load(f)
        return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data=load_json(saved_data)

    print(command)

    if command == 'save':
        key=input('Enter a key:')
        data[key]=clipboard.paste()
        save_items(saved_data,data)
        print("Data saved!")
    elif command == 'load':
        key = input('Enter a key:')
        if key in data:
            clipboard.copy(data[key])
        else:
            print("Key does not exist")

    elif command == 'list':
        print(data)
    else:
        print("Unknown command")
else:
    print("Pass exactly one command.")
