import random
import json

def randomize_array(arr):
    random.shuffle(arr)
    return arr

with open("ex2.json", 'r') as f:
  data = f.read()
  data = json.loads(data)

for arr in data:
  arr = randomize_array(arr)

with open("ex2.5.json", 'w') as f:
  f.write(json.dumps(data))