import json
from collections import defaultdict

d = json.load(open('hamnosys_prosodic_model.json'),"r")
hamnosys_to_prosodic = defaultdict(set)
prosodic_to_hamnosys = defaultdict(set)

for item in d:
    hamnosys_to_prosodic[item['letter']].add(item['prosodic'])
    hamnosys_to_prosodic[item['alt']].add(item['prosodic'])
    prosodic_to_hamnosys[item['prosodic']].add(item['letter'])
    hamnosys_to_prosodic[item['prosodic']].add(item['prosodic'])

#takes a string containing a hamnosys handshape e.g.  and returns a list of prosodic model equivalents
def hamnosys_to_prosodic(hamnosys):
    return hamnosys_to_prosodic[hamnosys]

#takes a string containing a prosodic model coding e.g. BT-;# and returns a list of hamnosys equivalents
def prosodic_to_hamnosys(prosodic):
    return prosodic_to_hamnosys[prosodic]


