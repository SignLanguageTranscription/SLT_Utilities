import json
from collections import defaultdict

d = json.load(open('signwriting_hamnosys_line.json'),"r")
hamnosys_to_sw = defaultdict(set)
sw_to_hamnosys = defaultdict(set)

for item in d:
    sw = item["letter"].split()[0]
    for symbol in range(ord(sw), ord(sw)+49):
        hamnosys_to_sw[item['transliteration']].add(symbol)
        hamnosys_to_sw[item['alt']].add(symbol)
        sw_to_hamnosys[symbol].add(item['transliteration'])
        hamnosys_to_sw[symbol].add(item['alt'])

#takes a string containing a hamnosys handshape e.g.  and returns a list of prosodic model equivalents
#conversion coverage is not always 100%, so this function may return an empty list
def hamnosys_to_signwriting(hamnosys):
    try:
        return hamnosys_to_prosodic[hamnosys]
    except:
        print("no matching signwriting found for: ", hamnosys)
        return []

#takes a string containing a prosodic model coding e.g. BT-;# and returns a list of hamnosys equivalents
#conversion coverage is not always 100%, so this function may return an empty list
def signwriting_to_hamnosys(prosodic):
    try:
        return prosodic_to_hamnosys[prosodic]
    except:
        print("no matching hamnosys found for: ", prosodic)
        return []

