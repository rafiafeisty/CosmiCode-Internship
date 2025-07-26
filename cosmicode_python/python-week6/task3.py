import json

data = {
    "name": "Rafia",
    "age": 20,
    "skills": ["Python", "React", "MongoDB"]
}

with open("data.json", "w") as write_file:
    json.dump(data, write_file, indent=3)
    print("Data written to 'data.json' successfully.")

with open("data.json", "r") as read_file:
    loaded_data = json.load(read_file)
    print("\nData read from 'data.json':")
    print(loaded_data)
