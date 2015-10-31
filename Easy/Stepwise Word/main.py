import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        longest = ''
        for word in line.split(' '):
            if len(word) > len(longest):
                longest = word
        
        print(' '.join([('*' * x + longest[x]) for x in range(len(longest))]))

lines.close()
 
