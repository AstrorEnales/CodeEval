import sys
import json

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        menu = json.loads(line)
        items = [x for x in menu['menu']['items'] if x != None]
        sum = 0
        for item in items:
            if 'label' in item:
                sum = sum + int(item['label'].replace('Label ', ''))
        print(sum)

lines.close()
