import json

numbers = [1 , 2 , 3 , 4 , 5 , "women"]
filename = "index.json"
with open(filename , "w") as file_thing:
    json.dump(numbers , file_thing)
