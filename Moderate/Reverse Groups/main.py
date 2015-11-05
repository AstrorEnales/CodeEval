import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers, times = line.split(';')
        times = int(times)
        numbers = numbers.split(',')
        parts = [numbers[i:(i + times)][::-1] if len(numbers) - i >= times else numbers[i:(i + times)] for i in range(0, len(numbers), times)]
        print(','.join([','.join(x) for x in parts]))

lines.close()
