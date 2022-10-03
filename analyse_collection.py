import json
from IPython import embed

with open("test_collections.txt", "r") as f:
    line = f.read()

data = json.loads(line)

embed()

