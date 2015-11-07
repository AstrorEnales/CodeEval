import sys

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def getDate(x):
    month, year = x.split(' ')
    return [months.index(month), int(year)]

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        ranges = [[getDate(y) for y in x.split('-')] for x in line.split('; ')]
        minyear = min([r[0][1] for r in ranges])
        maxyear = max([r[1][1] for r in ranges])
        timeline = [False] * ((maxyear - minyear + 1) * 12)
        for r in ranges:
            start = (r[0][1] - minyear) * 12 + r[0][0]
            end = (r[1][1] - minyear) * 12 + r[1][0]
            for i in range(start, end + 1):
                timeline[i] = True
        print(int(len([x for x in timeline if x]) / 12))

lines.close()
