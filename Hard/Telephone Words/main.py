import sys

lookup = {0: '0', 1: '1', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

def traverse(x, i, result, text):
    if i == len(x):
        result.append(text)
    else:
        for w in lookup[int(x[i])]:
            result = traverse(x, i + 1, result, text + w)
    return result

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        result = []
        result = traverse(line, 0, result, '')
        print(','.join(result))

lines.close()
